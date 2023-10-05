const reportForm = document.getElementById('report-form');
const reportList = document.getElementById('report-list');

reportForm.addEventListener('submit', (event) => {
  event.preventDefault(); 

  const patientName = document.getElementById('patient-name').value;
  const doctorName = document.getElementById('doctor-name').value;
  const reportDate = document.getElementById('report-date').value;
  const reportFile = document.getElementById('report-file').files[0];

  const reportItem = document.createElement('li');
  const reportLink = document.createElement('a');
  reportLink.textContent = `${patientName} - ${doctorName} - ${reportDate}`;
  reportLink.href = URL.createObjectURL(reportFile);
  reportLink.target = '_blank';
  reportItem.appendChild(reportLink);
  reportList.appendChild(reportItem);
});
document.addEventListener('click', (event) => {
    if (event.target.classList.contains('open-dialog-btn')) {
      const dialogBox = event.target.nextElementSibling;
      dialogBox.style.display = 'block';
    }
    if (event.target.classList.contains('close-dialog-btn')) {
      const dialogBox = event.target.closest('.report-dialog');
      dialogBox.style.display = 'none';
    }
  });