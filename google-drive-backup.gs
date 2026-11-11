/* MOMYIZZ - Backup automatik ke Google Drive
   1. Tukar KATA_RAHSIA di bawah kepada kata rahsia anda sendiri.
   2. Deploy > New deployment > Web app > Execute as: Me > Who has access: Anyone.
   3. Salin "Web app URL" dan tampal dalam worksheet (Backup > Google Drive). */
const KATA_RAHSIA = 'TUKAR_KATA_RAHSIA_INI';
const NAMA_FOLDER = 'Momyizz Backup';
const SIMPAN_MAKSIMUM = 60; // bilangan fail backup harian yang disimpan

function folder_() {
  const it = DriveApp.getFoldersByName(NAMA_FOLDER);
  return it.hasNext() ? it.next() : DriveApp.createFolder(NAMA_FOLDER);
}
function balas_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
function senaraiFail_(folder) {
  const out = [];
  const it = folder.getFiles();
  while (it.hasNext()) {
    const f = it.next();
    if (/^momyizz-backup-\d{4}-\d{2}-\d{2}\.json$/.test(f.getName())) out.push(f);
  }
  out.sort(function (a, b) { return b.getName() < a.getName() ? -1 : 1; });
  return out;
}
function doGet() {
  return balas_({ ok: true, info: 'Skrip backup Momyizz aktif.' });
}
function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    const body = JSON.parse(e.postData.contents);
    if (KATA_RAHSIA === 'TUKAR_KATA_RAHSIA_INI') return balas_({ ok: false, error: 'Tukar KATA_RAHSIA dalam skrip dahulu.' });
    if (body.key !== KATA_RAHSIA) return balas_({ ok: false, error: 'Kata rahsia tidak sepadan.' });
    const folder = folder_();
    if (body.action === 'ping') return balas_({ ok: true, folder: NAMA_FOLDER });
    if (body.action === 'save') {
      const hari = Utilities.formatDate(new Date(), 'Asia/Kuala_Lumpur', 'yyyy-MM-dd');
      const nama = 'momyizz-backup-' + hari + '.json';
      const isi = JSON.stringify(body.data);
      const ada = folder.getFilesByName(nama);
      if (ada.hasNext()) ada.next().setContent(isi);
      else folder.createFile(nama, isi, MimeType.PLAIN_TEXT);
      senaraiFail_(folder).slice(SIMPAN_MAKSIMUM).forEach(function (f) { f.setTrashed(true); });
      return balas_({ ok: true, file: nama });
    }
    if (body.action === 'latest') {
      const fail = senaraiFail_(folder);
      if (!fail.length) return balas_({ ok: false, error: 'Tiada fail backup dalam folder ' + NAMA_FOLDER + '.' });
      return balas_({ ok: true, file: fail[0].getName(), data: JSON.parse(fail[0].getBlob().getDataAsString()) });
    }
    return balas_({ ok: false, error: 'Tindakan tidak dikenali.' });
  } catch (err) {
    return balas_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}
