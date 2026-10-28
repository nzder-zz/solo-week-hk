"""Duo-Week-Planner.xlsx: every price is an input cell (blue); totals, shares and fit are formulas."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment

F = "Arial"
BLUE = Font(name=F, color="0000FF")
BLACK = Font(name=F)
GREEN = Font(name=F, color="008000")
BOLD = Font(name=F, bold=True)
HEAD = Font(name=F, bold=True, color="FFFFFF")
HFILL = PatternFill("solid", fgColor="241626")
YELLOW = PatternFill("solid", fgColor="FFFF00")
SOFT = PatternFill("solid", fgColor="F3EEF1")
EUR = '€#,##0;(€#,##0);-'
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(bottom=Side(style="thin", color="DDDDDD"))
STATUS_TXT = {"gf27": "Live, Google Flights 27 Oct", "est": "Estimate (schedule checked 28 Oct)"}
CHK = {"ok": "Open / fine", "warn": "Open, with a caveat", "out": "Closed or damaged: left out", "todo": "Still to verify"}
HOME_TXT = ["Fly home Fri", "Stay a night, fly Sat", "Back to HK with her"]


def header(ws, row, cols, widths=None):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font, cell.fill, cell.alignment = HEAD, HFILL, Alignment(wrap_text=True, vertical="center")
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[L(i)].width = w
    ws.freeze_panes = ws.cell(row=row + 1, column=1)


def put(ws, r, c, v, font=BLACK, fmt=None, wrap=False):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = font
    if fmt:
        cell.number_format = fmt
    if wrap:
        cell.alignment = WRAP
    return cell


def build_xlsx(D, path):
    wb = Workbook()
    fares = D["fares"]

    # ------------------------------------------------ Read me
    ws = wb.active
    ws.title = "Read me"
    ws.column_dimensions["A"].width = 110
    lines = [
        ("Week for two after Hong Kong — Sat 31 Oct → Fri 6 Nov 2026", BOLD),
        ("Seven trips × two plans (Slow, Fuller). Private rooms, taxis split, no Kyoto, no bike trips. She flies back to HK on Fri morning (her own flight leaves HK at 18:00).", BLACK),
        ("", BLACK),
        ("How to use", BOLD),
        ("• My plan: pick a trip, a plan and your way home from the drop-downs; the costs and both shares update.", BLACK),
        ("• Overview: every plan side by side, for each of your three ways home.", BLACK),
        ("• Change any blue number (Flights, Rooms, Plans, Inputs, Scores): every total is a formula.", BLACK),
        ("• Checks: what was verified on 28 Oct (Typhoon Champi damage, closures, volcano levels, fares) and what is still open.", BLACK),
        ("", BLACK),
        ("Colours", BOLD),
        ("Blue text = an input you can change · black = formula · green = link to another sheet · yellow fill = the choices on My plan.", BLACK),
        ("", BLACK),
        ("Price status", BOLD),
        ("Flights out and Saturday flights home: live fares from Google Flights, 27 Oct, for 1 adult (two seats can cost a little more).", BLACK),
        ("Her Friday flight back and your Friday flight home: schedules checked 28 Oct, prices are estimates — no browser was reachable to check them live.", BLACK),
        ("Rooms: typical prices for the cheapest decent private double in each place, not quotes.", BLACK),
        ("", BLACK),
        ("Your way home (always a single ticket)", BOLD),
        ("Fly home Fri: same day as her, land Sat 7 Nov.  Stay a night, fly Sat: one more day alone, land Sun 8 Nov (adds a room and a day of food).  Back to HK with her: same flight as hers, a night with the family, Etihad HK → Paris on Sat 19:45.", BLACK),
        ("", BLACK),
        ("Shares: each of you pays your own flights; rooms, food, transport, activities and misc are split 50/50.", BLACK),
        ("Rates used: 1 EUR = ¥177 · NT$36.5 · ₫28,967. Nothing is booked.", BLACK),
    ]
    for i, (t, f) in enumerate(lines, 1):
        put(ws, i, 1, t, f, wrap=True)

    # ------------------------------------------------ Inputs
    wi = wb.create_sheet("Inputs")
    header(wi, 1, ["Input", "Value", "Note"], [36, 12, 80])
    P = D["params"]
    rows = [("Days of food for two", P["days_together"], "Sat evening to Fri breakfast"),
            ("Misc per person (€)", P["misc_pp"], "SIM, tips, laundry"),
            ("Meal credit (share of a day's food)", P["meal_credit"], "When dinner + breakfast come with the room (temple, minshuku, ryokan)"),
            ("HK → Paris, Sat 7 Nov (€)", fares["hk_home"]["price"], fares["hk_home"]["detail"] + " · " + STATUS_TXT[fares["hk_home"]["status"]])]
    for i, (a, b, c) in enumerate(rows, 2):
        put(wi, i, 1, a); put(wi, i, 2, b, BLUE, "0.00" if isinstance(b, float) else EUR if "€" in a else "0"); put(wi, i, 3, c, wrap=True)
    DAYS, MISC, CREDIT, HKHOME = "Inputs!$B$2", "Inputs!$B$3", "Inputs!$B$4", "Inputs!$B$5"

    # ------------------------------------------------ Flights
    wf = wb.create_sheet("Flights")
    header(wf, 1, ["Key", "Leg", "Route", "Flight", "Price per person (€)", "Status", "Alternatives"], [16, 26, 13, 70, 14, 30, 70])
    r = 2
    for k, v in fares["out"].items():
        for col, val in enumerate([f"OUT|{k}", "Out, Sat 31 Oct (each)", v["route"], v["detail"], v["price"], STATUS_TXT[v["status"]], v["alt"]], 1):
            put(wf, r, col, val, BLUE if col == 5 else BLACK, EUR if col == 5 else None, wrap=col in (4, 7))
        r += 1
    for k, v in fares["her"].items():
        for col, val in enumerate([f"HER|{k}", "Her, Fri 6 Nov → HK", v["route"], v["detail"], v["price"], STATUS_TXT[v["status"]], v["alt"]], 1):
            put(wf, r, col, val, BLUE if col == 5 else BLACK, EUR if col == 5 else None, wrap=col in (4, 7))
        r += 1
    for k, v in fares["his"].items():
        for day in ("fri", "sat"):
            x = v[day]
            for col, val in enumerate([f"HIS{day.upper()}|{k}", f"You, home on {'Fri 6' if day == 'fri' else 'Sat 7'} Nov", x["route"], x["detail"], x["price"], STATUS_TXT[x["status"]], ""], 1):
                put(wf, r, col, val, BLUE if col == 5 else BLACK, EUR if col == 5 else None, wrap=col == 4)
            r += 1
    FL_LAST = r - 1
    FKEY, FPRICE = f"Flights!$A$2:$A${FL_LAST}", f"Flights!$E$2:$E${FL_LAST}"

    # ------------------------------------------------ Rooms
    wr = wb.create_sheet("Rooms")
    header(wr, 1, ["Plan key", "Trip", "Plan", "Night", "Where", "Room for two (€)", "Dinner + breakfast included"], [30, 40, 9, 12, 46, 14, 14])
    r = 2
    for d in D["dests"]:
        for o in d["options"]:
            key = f"{d['id']}|{o['style']}"
            for i, n in enumerate(o["nights"]):
                for col, val in enumerate([key, d["title"], o["style"], D["dates"][i], n["place"], n["room"], "Yes" if n["meals"] else "No"], 1):
                    put(wr, r, col, val, BLUE if col in (6, 7) else BLACK, EUR if col == 6 else None)
                r += 1
    RM_LAST = r - 1
    RKEY, RPRICE, RMEAL = f"Rooms!$A$2:$A${RM_LAST}", f"Rooms!$F$2:$F${RM_LAST}", f"Rooms!$G$2:$G${RM_LAST}"
    put(wr, r + 1, 1, "Typical rates for the cheapest decent private double, not quotes (checked 28 Oct). Change them to what you find on Booking/Agoda.", wrap=False)

    # ------------------------------------------------ Plans (the cost engine)
    wp = wb.create_sheet("Plans")
    cols = ["Plan key", "Trip", "Plan", "Food / day / person", "Rooms (6 n)", "Nights with meals", "Transport / person", "Shared taxis & cars",
            "Activities / person", "Your extra night alone", "Your extra day of food", "Flight out / person", "Her flight to HK", "Your flight Fri",
            "Your flight Sat", "Food for two", "Transport", "Activities", "Misc", "On the ground", "Total: fly home Fri", "Total: stay, fly Sat",
            "Total: back to HK with her", "Your share (Fri)", "Your share (Sat)", "Your share (HK)", "Her share", "Lookup", "Out key", "Her key", "Your key"]
    header(wp, 1, cols, [22, 36, 8] + [11] * 24 + [30, 14, 10, 10])
    r = 2
    plan_rows = {}
    for d in D["dests"]:
        for o in d["options"]:
            key = f"{d['id']}|{o['style']}"
            plan_rows[key] = r
            his_key = d["homes"]["fri"]["legs"][0]["route"]
            # keys for flight lookups
            out_k = [k for k, v in fares["out"].items() if v == d["out"]][0]
            her_k = [k for k, v in fares["her"].items() if v == d["her"]][0]
            his_k = [k for k, v in fares["his"].items() if v["fri"]["route"] == his_key][0]
            vals = {
                1: key, 2: d["title"], 3: o["style"], 4: d["food_day"],
                5: f"=SUMIFS({RPRICE},{RKEY},A{r})", 6: f'=COUNTIFS({RKEY},A{r},{RMEAL},"Yes")',
                7: o["transport_pp"], 8: o["shared"], 9: o["activities_pp"], 10: d["solo_night"], 11: d["solo_food"],
                12: f'=INDEX({FPRICE},MATCH("OUT|"&AC{r},{FKEY},0))', 13: f'=INDEX({FPRICE},MATCH("HER|"&AD{r},{FKEY},0))',
                14: f'=INDEX({FPRICE},MATCH("HISFRI|"&AE{r},{FKEY},0))', 15: f'=INDEX({FPRICE},MATCH("HISSAT|"&AE{r},{FKEY},0))',
                16: f"=2*D{r}*{DAYS}-2*{CREDIT}*D{r}*F{r}", 17: f"=2*G{r}+H{r}", 18: f"=2*I{r}", 19: f"=2*{MISC}",
                20: f"=E{r}+P{r}+Q{r}+R{r}+S{r}",
                21: f"=2*L{r}+M{r}+N{r}+T{r}", 22: f"=2*L{r}+M{r}+O{r}+J{r}+K{r}+T{r}", 23: f"=2*L{r}+M{r}+(M{r}+{HKHOME})+T{r}",
                24: f"=L{r}+N{r}+T{r}/2", 25: f"=L{r}+O{r}+J{r}+K{r}+T{r}/2", 26: f"=L{r}+M{r}+{HKHOME}+T{r}/2", 27: f"=L{r}+M{r}+T{r}/2",
                28: f'=B{r}&" | "&C{r}', 29: out_k, 30: her_k, 31: his_k,
            }
            for c, v in vals.items():
                inp = c in (4, 7, 8, 9, 10, 11)
                font = BLUE if inp else GREEN if c in (5, 6, 12, 13, 14, 15) else BLACK
                put(wp, r, c, v, font, EUR if 4 <= c <= 27 and c != 6 else None)
            r += 1
    PL_LAST = r - 1
    rng = lambda col: f"Plans!${col}$2:${col}${PL_LAST}"
    put(wp, r + 1, 1, "Food = 2 × food/day × days − meal credit for nights with dinner + breakfast. Transport = 2 × per person + shared. Shares: own flights + half of everything on the ground.", wrap=False)

    # ------------------------------------------------ Scores
    wsc = wb.create_sheet("Scores")
    crit = D["criteria"]
    header(wsc, 1, ["Trip"] + [c[1] for c in crit] + ["Fit /100", "Forecast /5 (27 Oct run)"], [40] + [11] * (len(crit) + 2))
    put(wsc, 2, 1, "Weight", BOLD)
    for j, (k, _) in enumerate(crit, 2):
        put(wsc, 2, j, D["weights"][k], BLUE)
    wcols = f"$B$2:${L(len(crit) + 1)}$2"
    score_row = {}
    for i, d in enumerate(D["dests"], 3):
        score_row[d["id"]] = i
        put(wsc, i, 1, d["title"])
        for j, (k, _) in enumerate(crit, 2):
            c = put(wsc, i, j, d["scores"][k], BLUE)
            if k == "weather":
                c.comment = Comment("Half the forecast score (ECMWF run of 27 Oct, 31 Oct–6 Nov), half the November climate.", "Claude")
        fc = len(crit) + 2
        put(wsc, i, fc, f"=ROUND(100*SUMPRODUCT(B{i}:{L(len(crit) + 1)}{i},{wcols})/(5*SUM({wcols})),0)")
        put(wsc, i, fc + 1, d["fc"]["score"], BLUE)
    FITCOL = L(len(crit) + 2)

    # ------------------------------------------------ Overview
    wo = wb.create_sheet("Overview", 1)
    header(wo, 1, ["Trip", "Plan", "Fit /100", "Forecast /5", "Places to sleep", "Transport (h)", "Fly home Fri", "Stay a night, fly Sat", "Back to HK with her", "Cheapest way home", "Your share (cheapest)", "Her share", "Route"],
           [40, 9, 9, 11, 10, 11, 13, 13, 13, 20, 13, 11, 90])
    r = 2
    for d in D["dests"]:
        for o in d["options"]:
            pr = plan_rows[f"{d['id']}|{o['style']}"]
            sr = score_row[d["id"]]
            put(wo, r, 1, d["title"]); put(wo, r, 2, o["style"])
            put(wo, r, 3, f"=Scores!{FITCOL}{sr}", GREEN)
            put(wo, r, 4, f"=Scores!{L(len(crit) + 3)}{sr}", GREEN)
            put(wo, r, 5, o["beds"]); put(wo, r, 6, round(o["travel"] / 60, 1), fmt="0.0")
            put(wo, r, 7, f"=Plans!U{pr}", GREEN, EUR); put(wo, r, 8, f"=Plans!V{pr}", GREEN, EUR); put(wo, r, 9, f"=Plans!W{pr}", GREEN, EUR)
            put(wo, r, 10, f'=IF(G{r}=MIN(G{r}:I{r}),"Fly home Fri",IF(H{r}=MIN(G{r}:I{r}),"Stay a night, fly Sat","Back to HK with her"))')
            put(wo, r, 11, f"=IF(J{r}=\"Fly home Fri\",Plans!X{pr},IF(J{r}=\"Stay a night, fly Sat\",Plans!Y{pr},Plans!Z{pr}))", fmt=EUR)
            put(wo, r, 12, f"=Plans!AA{pr}", GREEN, EUR)
            put(wo, r, 13, " → ".join(o["route"]), wrap=False)
            r += 1
    put(wo, r + 1, 1, "Totals are for the two of you, in euros. Places to sleep counts distinct towns; transport counts every leg from Central on Sat to the airport on Fri.")

    # ------------------------------------------------ My plan
    wm = wb.create_sheet("My plan", 1)
    wm.column_dimensions["A"].width = 34; wm.column_dimensions["B"].width = 46; wm.column_dimensions["C"].width = 60
    put(wm, 1, 1, "My plan: pick from the yellow cells", BOLD)
    trips = [d["title"] for d in D["dests"]]
    put(wm, 3, 1, "Trip"); c = put(wm, 3, 2, D["dests"][4]["title"]); c.fill = YELLOW
    put(wm, 4, 1, "Plan"); c = put(wm, 4, 2, "Slow"); c.fill = YELLOW
    put(wm, 5, 1, "Your way home"); c = put(wm, 5, 2, "Fly home Fri"); c.fill = YELLOW
    # lists for validation
    for i, t in enumerate(trips, 1):
        put(wm, i, 26, t)
    for i, t in enumerate(HOME_TXT, 1):
        put(wm, i, 27, t)
    wm.column_dimensions["Z"].hidden = True; wm.column_dimensions["AA"].hidden = True
    dv1 = DataValidation(type="list", formula1=f"=$Z$1:$Z${len(trips)}", allow_blank=False)
    dv2 = DataValidation(type="list", formula1='"Slow,Fuller"', allow_blank=False)
    dv3 = DataValidation(type="list", formula1="=$AA$1:$AA$3", allow_blank=False)
    for dv, cell in ((dv1, "B3"), (dv2, "B4"), (dv3, "B5")):
        wm.add_data_validation(dv); dv.add(cell)
    put(wm, 6, 1, "Row in Plans"); put(wm, 6, 2, f'=MATCH(B3&" | "&B4,{rng("AB")},0)')
    put(wm, 7, 1, "Home option (1–3)"); put(wm, 7, 2, '=MATCH(B5,$AA$1:$AA$3,0)')
    lines = [
        ("Flights out, both of you", f'=2*INDEX({rng("L")},B6)'),
        ("Her flight back to HK", f'=INDEX({rng("M")},B6)'),
        ("Your way home", f'=CHOOSE(B7,INDEX({rng("N")},B6),INDEX({rng("O")},B6)+INDEX({rng("J")},B6)+INDEX({rng("K")},B6),INDEX({rng("M")},B6)+{HKHOME})'),
        ("Rooms, 6 nights", f'=INDEX({rng("E")},B6)'),
        ("Food for two", f'=INDEX({rng("P")},B6)'),
        ("Transport (trains, buses, shared taxis)", f'=INDEX({rng("Q")},B6)'),
        ("Activities", f'=INDEX({rng("R")},B6)'),
        ("Misc", f'=INDEX({rng("S")},B6)'),
    ]
    r0 = 9
    put(wm, r0, 1, "Cost", BOLD); put(wm, r0, 2, "€", BOLD)
    for i, (a, f) in enumerate(lines, r0 + 1):
        put(wm, i, 1, a); put(wm, i, 2, f, GREEN, EUR)
    tr = r0 + len(lines) + 1
    put(wm, tr, 1, "Total for two", BOLD); put(wm, tr, 2, f"=SUM(B{r0 + 1}:B{tr - 1})", BOLD, EUR)
    put(wm, tr + 1, 1, "Check: matches Plans total"); put(wm, tr + 1, 2, f'=IF(ABS(B{tr}-CHOOSE(B7,INDEX({rng("U")},B6),INDEX({rng("V")},B6),INDEX({rng("W")},B6)))<0.5,"OK","Mismatch")')
    put(wm, tr + 3, 1, "Your share", BOLD); put(wm, tr + 3, 2, f'=CHOOSE(B7,INDEX({rng("X")},B6),INDEX({rng("Y")},B6),INDEX({rng("Z")},B6))', BOLD, EUR)
    put(wm, tr + 4, 1, "Her share", BOLD); put(wm, tr + 4, 2, f'=INDEX({rng("AA")},B6)', BOLD, EUR)
    put(wm, tr + 5, 1, "Fit /100"); put(wm, tr + 5, 2, f'=INDEX(Overview!$C$2:$C${1 + PL_LAST - 1},B6)', GREEN)
    put(wm, tr + 7, 1, "Each of you pays your own flights; everything on the ground is split 50/50.", wrap=False)

    # ------------------------------------------------ Day by day
    wd = wb.create_sheet("Day by day")
    header(wd, 1, ["Trip", "Plan", "Day", "Date", "Title", "Pace", "Morning", "Afternoon", "Evening", "Sleep", "If it rains", "Transport (min)", "Legs"],
           [30, 8, 5, 11, 30, 8, 45, 45, 35, 24, 30, 10, 50])
    r = 2
    for d in D["dests"]:
        for o in d["options"]:
            for i, x in enumerate(o["days"]):
                vals = [d["short"], o["style"], i + 1, D["dates"][i], x["t"], x["e"], x["am"], x["pm"], x["eve"], x["sleep"], x["b"] or "",
                        sum(l[2] for l in x["tr"]), " · ".join(f"{l[1]} ({l[2]} min)" for l in x["tr"])]
                for c, v in enumerate(vals, 1):
                    put(wd, r, c, v, wrap=c in (5, 7, 8, 9, 11, 13))
                r += 1

    # ------------------------------------------------ Checks
    wc = wb.create_sheet("Checks")
    header(wc, 1, ["Where", "What", "Status", "Finding", "Source", "Link"], [10, 34, 26, 80, 30, 50])
    order = {"out": 0, "todo": 1, "warn": 2, "ok": 3}
    for i, c in enumerate(sorted(D["checks"], key=lambda c: order[c[2]]), 2):
        for j, v in enumerate([c[0], c[1], CHK[c[2]], c[3], c[4], c[5]], 1):
            cell = put(wc, i, j, v, wrap=j == 4)
            if j == 6:
                cell.hyperlink = v; cell.font = Font(name=F, color="0563C1", underline="single")
            if j == 3:
                cell.fill = PatternFill("solid", fgColor={"ok": "DDF0E3", "warn": "FBEBD0", "out": "F6D7D5", "todo": "EEEEEE"}[c[2]])
    put(wc, len(D["checks"]) + 3, 1, f"Checked {D['checked']}.")

    # ------------------------------------------------ Sources
    wsr = wb.create_sheet("Sources")
    header(wsr, 1, ["Source", "Link", "Note"], [60, 70, 40])
    for i, (n, u, note) in enumerate(D["sources"], 2):
        put(wsr, i, 1, n); c = put(wsr, i, 2, u); c.hyperlink = u; c.font = Font(name=F, color="0563C1", underline="single"); put(wsr, i, 3, note)

    for w in wb.worksheets:
        for row in w.iter_rows():
            for cell in row:
                if cell.font and cell.font.name != F:
                    cell.font = Font(name=F, bold=cell.font.bold, color=cell.font.color)
    wb.save(path)
