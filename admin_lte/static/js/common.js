// Function to show toast notifications
function showToast(message, type = "success", duration = 3000) {
  const toastContainer = document.getElementById("toast-container");
  const toast = document.createElement("div");

  // Set toast class based on type
  toast.className = `toast alert alert-${type}`;
  toast.style.display = "block";
  toast.style.marginBottom = "10px";
  toast.innerHTML = `<strong>${
    type === "success" ? "Success" : "Error"
  }:</strong> ${message}`;

  // Append toast to the container
  toastContainer.appendChild(toast);

  // Auto-remove the toast after the specified duration
  setTimeout(() => {
    toast.remove();
  }, duration);
}
