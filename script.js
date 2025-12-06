// 滑動動畫
document.querySelectorAll(".section").forEach((sec) => {
    sec.addEventListener("mouseover", () => {
        sec.style.transition = "0.3s";
        sec.style.background = "#4d85aaff";
    });
    sec.addEventListener("mouseout", () => {
        sec.style.background = "white";
    });
});

// 點擊 Skills 自動滑動
document.getElementById("skills").addEventListener("click", () => {
    window.scrollTo({ top: 1200, behavior: "smooth" });
});
