const root = document.querySelector("[data-carousel]");
const track = document.querySelector("[data-carousel-track]");
const prev = document.querySelector(".carousel-prev");
const next = document.querySelector(".carousel-next");
const filters = document.querySelectorAll(".filter-chip");

function visibleCards() {
  return [...document.querySelectorAll("[data-use-case]:not([hidden])")];
}

function cardStep() {
  const first = visibleCards()[0];
  if (!first || !track) return 320;
  const styles = getComputedStyle(track);
  const gap = parseFloat(styles.columnGap || styles.gap || "0");
  return first.getBoundingClientRect().width + gap;
}

prev?.addEventListener("click", () => {
  track?.scrollBy({ left: -cardStep(), behavior: "smooth" });
});

next?.addEventListener("click", () => {
  track?.scrollBy({ left: cardStep(), behavior: "smooth" });
});

filters.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;
    filters.forEach((item) => item.classList.remove("active"));
    button.classList.add("active");

    document.querySelectorAll("[data-use-case]").forEach((card) => {
      const categories = (card.dataset.category || "").split(/\s+/);
      card.hidden = filter !== "all" && !categories.includes(filter);
    });

    track?.scrollTo({ left: 0, behavior: "smooth" });
  });
});
