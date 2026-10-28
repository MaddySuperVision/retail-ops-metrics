# Retail store operations metrics

Plain definitions, formulas and free templates for measuring what happens on a retail store floor: customer-to-staff ratio, checkout wait time, scheduled vs deployed labor, and why sales per labor hour can hide understaffing.

Maintained by [Super Vision](https://www.supervision.work/), which builds operational intelligence for multi-location retail from the cameras stores already have. Everything here works without our product: a door counter, your POS and a spreadsheet are enough to start.

## Contents

| File | What it is |
|---|---|
| [hourly-coverage.csv](hourly-coverage.csv) | Hour-by-hour template: entries, shoppers present, associates scheduled and on the floor, transactions |
| [queue-snapshots.csv](queue-snapshots.csv) | Checkout line count template for a two-hour peak window |
| [store_metrics.py](store_metrics.py) | Small Python calculator (no dependencies) for the formulas below, run against the templates |
| [Google Sheets calculator](https://docs.google.com/spreadsheets/d/17FrI0pWOV8FY-quwBtz-fyPrtT3dUH7uoOvv97SaCUg/copy) | Free Google Sheets version of both templates with the formulas built in (hypothetical example data). The link makes your own editable copy |

## Customer-to-staff ratio

Two different measurements share this name.

**Flow ratio (planning):** shopper entries in an hour divided by staff hours worked in that hour.

**Concurrent ratio (service):** average shoppers present divided by average associates actually on the sales floor.

Estimate shoppers present with Little's Law:

```
shoppers present ≈ entries per hour × average visit length (hours)
```

60 entries an hour with a 17 minute average visit is about 17 shoppers present.

Measure by hour and by zone, never as a daily average. Set your threshold from your own data: bucket four weeks of hours by ratio and find where conversion starts to drop.

**Labor-to-traffic ratio:** the flow ratio read the other way, labor hours per 100 entries. State the direction every time, because the names are used loosely.

```
labor-to-traffic ratio = staff hours in the hour ÷ shopper entries in the hour × 100
peak-hour maximum ratio = highest hourly (shoppers present ÷ associates on the floor) in the day
```

Report the peak-hour maximum and the hour it happened next to the daily average and the number of hours above your threshold. A day can average 5 shoppers per associate on the floor and still reach 10 at 13:00.

Full guide: [Customer-to-staff ratio in retail](https://www.supervision.work/guides/customer-to-staff-ratio/)

Further reading: [Customer-to-staff ratio in retail: your daily number is hiding your worst two hours](https://www.linkedin.com/pulse/customer-to-staff-ratio-retail-your-daily-number-hiding-maddy-sukoru-qronc/) (LinkedIn article by Maddy Sukoru)

## Checkout wait time

- **Wait time:** joining the line until reaching the register. Your POS cannot see it.
- **Service time:** the transaction itself. This is what POS timestamps measure.
- **Balking:** a shopper sees the line and never joins. **Reneging:** joins, then leaves. Neither reaches the POS.

Estimate average wait without a stopwatch (Little's Law):

```
average wait (minutes) = average queue length ÷ checkouts completed per minute
```

Report the median and 90th percentile wait, minutes per day above your target, peak line length, and whether every register that should have been open was staffed in those minutes. Rank stores by minutes above target, not average wait.

Full guide: [How to measure checkout wait time](https://www.supervision.work/guides/checkout-wait-time/)

Further reading: [How to measure checkout wait time: a two-hour test any store can run this Saturday](https://www.linkedin.com/pulse/how-measure-checkout-wait-time-two-hour-test-any-store-maddy-sukoru-vdatc/) (LinkedIn article by Maddy Sukoru)

## Sales per labor hour

```
SPLH = net sales ÷ labor hours worked
```

SPLH tends to rise when a store runs short at peak: hours fall, and sales lost to unattended shoppers and long lines never appear anywhere. Read it next to hourly conversion and minutes above your checkout target.

Full guide: [Is sales per labor hour a good KPI?](https://www.supervision.work/guides/sales-per-labor-hour/)

Further reading: [Is sales per labor hour a good KPI? Good at finding waste, bad at ranking stores](https://www.linkedin.com/pulse/sales-per-labor-hour-good-kpi-finding-waste-bad-ranking-maddy-sukoru-2xgvc/) (LinkedIn article by Maddy Sukoru)

## Scheduled vs deployed labor

Scheduled is who is on the rota. Deployed is who is on the floor, at the right position, in that hour. Breaks, receiving, replenishment and online order picking create the gap, and it is usually largest in the busiest hour.

```
deployment rate = deployed hours ÷ worked hours (same time block)
coverage gap = customer-facing hours scheduled − deployed hours (same time block)
```

Six associates clocked in from 12:00 to 13:00 with floor counts averaging 3.5 is a 58% deployment rate. Read both by hour or 15-minute block, never only for the day.

Full guide: [Scheduled vs deployed labor in retail](https://www.supervision.work/guides/scheduled-vs-deployed-labor/)

Further reading: [Scheduled vs deployed labor in retail: six on the schedule, two on the floor at the peak](https://www.linkedin.com/pulse/scheduled-vs-deployed-labor-retail-six-schedule-two-floor-sukoru-9cikc/) (LinkedIn article by Maddy Sukoru)

## Research worth reading

- Perdikaki, Kesavan, Swaminathan (2012). Effect of traffic on sales and conversion rates of retail stores. *Manufacturing & Service Operations Management*. DOI 10.1287/msom.1110.0356
- Mani, Kesavan, Swaminathan (2015). Estimating the impact of understaffing on sales and profitability in retail stores. *Production and Operations Management*. All 41 stores studied were systematically understaffed during peak hours.
- Lu, Musalem, Olivares, Schilkrut (2013). Measuring the effect of queues on customer purchases. *Management Science*. DOI 10.1287/mnsc.1120.1686
- Chuang, Oliva, Perdikaki (2016). Traffic-based labor planning in retail stores. *Production and Operations Management*.
- Knowledge at Wharton (2019). [Retail's big mistake: slashing payroll cuts into profits](https://knowledge.wharton.upenn.edu/article/retail-staffing-model)

## License

MIT for the code, CC BY 4.0 for the text and templates. Use them, change them, share them.
