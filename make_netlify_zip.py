import zipfile, os

script_dir = os.path.dirname(os.path.abspath(__file__))

files_to_add = {
    'index.html':                              'vibe-website-redesign.html',
    'infographic.html':                        'VIBE_Recognition_Infographic.html',
    'terms.html':                               'terms-and-conditions.html',
    'resources.html':                           'resources.html',
    'library.html':                              'library.html',
    'portal.html':                               'portal.html',
    'VIBE_Overview_Pamphlet.pdf':                'VIBE_Overview_Pamphlet.pdf',
    'VIBE_Module_Recognition.pdf':                'VIBE_Module_Recognition.pdf',
    'VIBE_Module_WHS_and_Incident_Reporting.pdf': 'VIBE_Module_WHS_and_Incident_Reporting.pdf',
    'VIBE_Module_PL_Event_Booking.pdf':           'VIBE_Module_PL_Event_Booking.pdf',
    'VIBE_Module_VIBE_Pulse_Wellbeing.pdf':       'VIBE_Module_VIBE_Pulse_Wellbeing.pdf',
    'VIBE_Module_Staff_Scheduler.pdf':            'VIBE_Module_Staff_Scheduler.pdf',
    'VIBE_Module_Staff_Scheduler_School_Edition.pdf': 'VIBE_Module_Staff_Scheduler_School_Edition.pdf',
    'VIBE_Pricing_Structure.pdf':                 'VIBE_Pricing_Structure.pdf',
    'favicon.png':                                os.path.join('public','branding','favicon.png'),
    'sitemap.xml':                                'sitemap.xml',
}

zip_path = os.path.join(script_dir, 'netlify-deploy.zip')

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    # Redirect rules — clean URLs
    zf.writestr('_redirects', '/  /index.html  200\n/terms  /terms.html  200\n/library  /library.html  200\n/portal  /portal.html  200\n')

    for zip_name, local_name in files_to_add.items():
        local_path = os.path.join(script_dir, local_name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                zf.writestr(zip_name, f.read())
            print(f"  + {local_name} → {zip_name}")
        else:
            print(f"  ⚠ {local_name} not found — skipped")

print("Done. Created " + zip_path)