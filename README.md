# NGB CARE Team – Contact Hub (Option 1)

This package contains:
- `index.html` – mobile-friendly contact directory page
- 5 individual vCards (`.vcf`) – one per contact
- `qr-code.png` – QR code (generated from a placeholder URL)
- `generate_qr.py` – script to generate a new QR code once you know the final URL

## Quick start (local preview)
Open `index.html` in a browser. The "Save Contact" buttons download the vCards.

## Hosting (recommended: simple static hosting)
Any static host works (SharePoint static site, GitHub Pages, S3, etc.). Upload all files together to the same folder.

### GitHub Pages (no coding)
1. Create a new GitHub repository (public) named e.g., `ngb-care-contacts`
2. Upload all files from this folder into the repo root
3. In repo Settings → Pages → set Source to `Deploy from a branch` (main / root)
4. Your URL will look like: `https://<username>.github.io/ngb-care-contacts/`

## Regenerating the QR code
Once you have the final URL, run:

```bash
python3 generate_qr.py "https://YOUR-FINAL-URL-HERE"
```

That will overwrite `qr-code.png` with the correct QR.

