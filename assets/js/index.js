(() => {
	const yearEl = document.getElementById("year");
	if (yearEl) yearEl.textContent = String(new Date().getFullYear());
})();

(() => {
	const grid = document.getElementById("tours-grid");
	const errorEl = document.getElementById("tours-error");
	if (!grid) return;

	const setError = (message) => {
		if (!errorEl) return;
		errorEl.hidden = false;
		errorEl.textContent = message;
	};

	const escapeHtml = (value) => {
		const div = document.createElement("div");
		div.textContent = String(value ?? "");
		return div.innerHTML;
	};

	const render = (tours) => {
		if (!Array.isArray(tours) || tours.length === 0) {
			grid.innerHTML = "";
			setError("No tours found. Add a tour folder and re-run the manifest generator.");
			return;
		}

		grid.innerHTML = tours
			.map((t) => {
				const title = escapeHtml(t.title || t.slug || "Tour");
				const href = escapeHtml(t.href || "#");
				const preview = t.preview ? escapeHtml(t.preview) : "";
				const media = preview
					? `<img class="tour-card__img" src="${preview}" alt="${title}" loading="lazy" />`
					: `<div class="tour-card__img tour-card__img--fallback" aria-hidden="true"></div>`;

				return `
					<a class="tour-card" href="${href}">
						<div class="tour-card__media">${media}</div>
						<div class="tour-card__body">
							<div class="tour-card__title">${title}</div>
							<div class="tour-card__meta">Open tour</div>
						</div>
					</a>
				`;
			})
			.join("");
	};

	const load = async () => {
		try {
			const res = await fetch(`assets/data/tours.json?v=${Date.now()}`, { cache: "no-store" });
			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			const data = await res.json();
			render(data.tours);
		} catch (e) {
			grid.innerHTML = "";
			setError(
				"Could not load tour list. Generate assets/data/tours.json by running: python3 assets/scripts/generate_tours_manifest.py"
			);
		}
	};

	void load();
})();
