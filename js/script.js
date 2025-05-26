function showSection(sectionId) {
  document.querySelectorAll(".content-section").forEach(sec => {
    sec.classList.add("hidden");
  });

  document.getElementById(sectionId).classList.remove("hidden");

  const teamSection = document.getElementById("team");
  if (sectionId === "team") {
    teamSection.classList.remove("hidden");
  } else {
    teamSection.classList.add("hidden");
  }

  if (window.innerWidth < 768) {
    document.getElementById("sidebar").classList.add("hidden");
  }
}

document.getElementById("menu-toggle").addEventListener("click", () => {
  document.getElementById("sidebar").classList.toggle("hidden");
});

window.addEventListener("resize", () => {
  if (window.innerWidth >= 768) {
    document.getElementById("sidebar").classList.remove("hidden");
  } else {
    document.getElementById("sidebar").classList.add("hidden");
  }
});