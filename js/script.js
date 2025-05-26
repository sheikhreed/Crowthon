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

document.querySelectorAll("code").forEach((block) => {
  const lang = block.className.split("-")[1];
  const code = block.textContent;

  const highlighted = code
    .replace(/"(.*?)"/g, '<span class="token string">"$1"</span>')
    .replace(/\b(def|print|function|const|let|var|echo|return)\b/g, '<span class="token keyword">$1</span>') // Keywords
    .replace(/(#.*)/g, '<span class="token comment">$1</span>')
    .replace(/\b\d+\b/g, '<span class="token number">$&</span>');

  block.innerHTML = highlighted;
});