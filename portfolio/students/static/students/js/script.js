console.log("Student Management System Loaded");

document.addEventListener("DOMContentLoaded", () => {

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(alert => {

        setTimeout(() => {

            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);

            bsAlert.close();

        }, 3000);

    });

});