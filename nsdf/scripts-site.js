const toggle = document.querySelector(".menu-toggle");
const menu = document.querySelector("#mobile-menu");
const bottomMenu = document.querySelector(".bottom-menu-button");

function setMenu(open) {
  if (!toggle || !menu) return;
  toggle.setAttribute("aria-expanded", String(open));
  menu.hidden = !open;
}

toggle?.addEventListener("click", () => {
  setMenu(toggle.getAttribute("aria-expanded") !== "true");
});

bottomMenu?.addEventListener("click", () => {
  const open = toggle?.getAttribute("aria-expanded") !== "true";
  setMenu(open);
  if (open) window.scrollTo({ top: 0, behavior: "smooth" });
});

menu?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => setMenu(false));
});

window.addEventListener("resize", () => {
  if (window.innerWidth > 760) setMenu(false);
});
