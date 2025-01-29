const basePath = window.location.origin + "/";

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".delete-btn").forEach((button) => {
      button.addEventListener("click", function (event) {
          event.preventDefault();
          let itemId = this.getAttribute("data-id");

          if (!confirm("Are you sure you want to delete this state?")) return;

          fetch(`/state/delete/${itemId}/`, {
              method: "DELETE",
              headers: {
                  "X-CSRFToken": getCSRFToken(),
                  "Content-Type": "application/json",
              },
          })
              .then((response) => response.json())
              .then((data) => {
                  if (data.message) {
                      // alert(data.message);
                      location.reload();
                  } else {
                      alert(data.error);
                  }
              })
              .catch((error) => console.error("Error:", error));
      });
  });
});

// Function to get CSRF token from cookies (for Django)
function getCSRFToken() {
  let cookieValue = null;
  let cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.startsWith("csrftoken=")) {
          cookieValue = cookie.substring("csrftoken=".length, cookie.length);
          break;
      }
  }
  return cookieValue;
}


// function handleSubmit(event) {
//   // Prevent form from submitting the traditional way
//   event.preventDefault();

//   // Collect form data dynamically
//   const formData = new FormData(document.getElementById("user-form"));

//   // Prepare the request payload dynamically
//   const data = {};
//   formData.forEach((value, key) => {
//     data[key] = value;  // Assign each form element's name and value to the data object
//   });
 
//   // Send the request using fetch
//   fetch("/add-state/", {
//     method: "POST",
//     headers: {
//       "X-Requested-With": "XMLHttpRequest",
//       "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value, // CSRF Token
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(data), // Send the data as JSON
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.status === "success") {
//         // alert("State added successfully!");
//         location.reload(); // Reload the page or update the UI accordingly
//       } else {
//         console.error(data.message || "An error occurred.");
//       }
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//       alert("An error occurred.");
//     });
// }

function handleSubmit(event) {
  event.preventDefault();

  const form = document.getElementById("user-form");

  // Extract the URL and method dynamically
  const formAction = form.getAttribute("data-url"); // Get the URL from the form's data-url attribute
  const formMethod = form.getAttribute("method") ; // Default to POST if not specified
  // alert(formAction);
  // Collect form data dynamically
  const formData = new FormData(form);

  // Prepare the request payload dynamically
  const data = {};
  formData.forEach((value, key) => {
    data[key] = value;  // Assign each form element's name and value to the data object
  });

  // Send the request using fetch
  fetch(formAction, {
    method: formMethod,  // Use the dynamically obtained method
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value, // CSRF Token
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data), // Send the data as JSON
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        location.reload(); // Reload the page or update the UI accordingly
      } else {
        console.error(data.message || "An error occurred.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred.");
    });
}


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

// const addEditModal = async (id, module_name, module_function, formmethod) => {
//   let url = id
//     ? `${basePath}${module_name}/${id}/${module_function}`
//     : `${basePath}${module_name}/${module_function}`;
//   // alert(url);

//   try {
//     const response = await fetchData(url, {
//       method: formmethod,
//       headers: { "Content-Type": "text/html" },
//     });
//     const html = await response.text();
//     const modalContent = document.querySelector("#modal-content");
//     if (modalContent) {
//       modalContent.innerHTML = html;
//       $("#modal-sm").modal("show");
//       attachModalEventListeners();
//     } else {
//       console.error('Element "#modal-content" not found.');
//     }
//   } catch (error) {
//     alert("An error occurred. Please try again.");
//   }
// };

const addEditModal = async (id, module_name, module_function, formmethod) => {
  let url = id
    ? `${basePath}${module_name}/${id}/${module_function}`
    : `${basePath}${module_name}/${module_function}`;

  try {
    const response = await fetch(url, { method: formmethod });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const html = await response.text();
    const modalContent = document.querySelector("#modal-content");

    if (modalContent) {
      modalContent.innerHTML = html;
      $("#modal-sm").modal("show"); // Ensure Bootstrap Modal Opens
    } else {
      console.error('Element "#modal-content" not found.');
    }
  } catch (error) {
    console.error("Error loading modal:", error);
    alert("An error occurred. Please try again.");
  }
};

// Function to handle the delete action


// Event listener to trigger the deleteItem function on clicking the delete button


