/* ============================================================
   StudySync — interactions
   ============================================================ */

(function () {
  "use strict";

  /* ---------- Sidebar (mobile) ---------- */
  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("sidebar-overlay");
  const hamburger = document.getElementById("hamburger");

  function closeSidebar() {
    if (!sidebar) return;
    sidebar.classList.remove("open");
    if (overlay) overlay.classList.remove("show");
  }

  if (hamburger && sidebar) {
    hamburger.addEventListener("click", function () {
      sidebar.classList.toggle("open");
      if (overlay) overlay.classList.toggle("show");
    });
  }

  if (overlay) {
    overlay.addEventListener("click", closeSidebar);
  }

  /* Close sidebar after navigating (mobile) */
  document.querySelectorAll(".sidebar .nav-link").forEach(function (link) {
    link.addEventListener("click", closeSidebar);
  });

  /* ---------- User dropdown menu ---------- */
  document.querySelectorAll(".user-menu").forEach(function (menu) {
    const btn = menu.querySelector(".user-menu-btn");
    const dropdown = menu.querySelector(".dropdown");

    if (!btn || !dropdown) return;

    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      const isOpen = dropdown.classList.contains("open");
      closeAllDropdowns();
      if (!isOpen) dropdown.classList.add("open");
    });
  });

  function closeAllDropdowns() {
    document.querySelectorAll(".dropdown").forEach(function (d) {
      d.classList.remove("open");
    });
  }

  document.addEventListener("click", closeAllDropdowns);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeAllDropdowns();
  });

  /* ---------- Auto-dismiss toasts ---------- */
  document.querySelectorAll(".toast").forEach(function (toast) {
    const delay = parseInt(toast.dataset.delay || "4200", 10);

    setTimeout(function () {
      toast.classList.add("out");
      setTimeout(function () {
        toast.remove();
      }, 320);
    }, delay);
  });

  /* ---------- Lightweight form guards ---------- */
  document.querySelectorAll("form[data-confirm]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      const message = form.dataset.confirm || "Are you sure?";
      if (!window.confirm(message)) {
        e.preventDefault();
      }
    });
  });

  /* ---------- Toggle chapter completion checkbox visual feedback ---------- */
  document.querySelectorAll('input[type="checkbox"][data-autosubmit]').forEach(function (cb) {
    cb.addEventListener("change", function () {
      const form = cb.closest("form");
      if (form) form.submit();
    });
  });
})();
