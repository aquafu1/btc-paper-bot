# Backtest report (FAKE money)

Data: Coinbase BTC-USD 1-min candles, Oct 19 16:35 UTC to Nov 09 17:35 UTC (21 days).
Assumed entry price 0.51, fee 1.5% of stake, $10 per trade. Break-even win rate = 51.8%.

**Train** = first 14 days (where you'd pick a strategy). **Test** = last 7 days (did it still work on data it wasn't picked on?).

| Strategy | Trades | Win % | P&L (all) | Train P&L | Test P&L | Test win % | Verdict |
|---|---|---|---|---|---|---|---|
| reversal_5m_0.10pct | 434 | 52.8 | $+85 | $+155 | $-70 | 49.7 | can't tell from luck |
| reversal_5m_0.00pct | 2015 | 52.0 | $+77 | $+143 | $-66 | 51.3 | can't tell from luck |
| momentum_15m_0.30pct | 163 | 46.6 | $-164 | $+66 | $-230 | 35.2 | can't tell from luck |
| reversal_5m_0.30pct | 35 | 54.3 | $+17 | $+44 | $-27 | 45.0 | too few trades |
| momentum_60m_0.30pct | 521 | 48.4 | $-347 | $+43 | $-390 | 41.4 | can't tell from luck |
| reversal_15m_0.10pct | 835 | 52.2 | $+74 | $+29 | $+45 | 52.5 | can't tell from luck |
| momentum_5m_0.30pct | 35 | 45.7 | $-42 | $-54 | $+13 | 55.0 | too few trades |
| reversal_15m_0.30pct | 163 | 53.4 | $+51 | $-130 | $+181 | 64.8 | can't tell from luck |
| reversal_60m_0.10pct | 1364 | 52.3 | $+136 | $-227 | $+363 | 55.8 | can't tell from luck |
| trend_filter | 527 | 45.7 | $-624 | $-239 | $-385 | 40.7 | losing for real |
| reversal_60m_0.30pct | 521 | 51.6 | $-14 | $-271 | $+257 | 58.6 | can't tell from luck |
| reversal_15m_0.00pct | 2015 | 51.5 | $-119 | $-289 | $+170 | 53.1 | can't tell from luck |
| reversal_60m_0.00pct | 2015 | 51.6 | $-60 | $-328 | $+268 | 53.8 | can't tell from luck |
| momentum_5m_0.10pct | 434 | 47.2 | $-385 | $-335 | $-51 | 50.3 | can't tell from luck |
| coinflip | 2015 | 49.8 | $-766 | $-347 | $-418 | 48.6 | can't tell from luck |
| momentum_15m_0.10pct | 835 | 47.8 | $-652 | $-403 | $-249 | 47.5 | losing for real |
| momentum_60m_0.10pct | 1364 | 47.7 | $-1080 | $-404 | $-676 | 44.2 | losing for real |
| momentum_60m_0.00pct | 2015 | 48.4 | $-1335 | $-602 | $-732 | 46.2 | losing for real |
| momentum_15m_0.00pct | 2015 | 48.5 | $-1276 | $-642 | $-634 | 46.9 | losing for real |
| momentum_5m_0.00pct | 2015 | 48.0 | $-1472 | $-1073 | $-399 | 48.7 | losing for real |
| always_up | 2015 | 48.0 | $-1472 | $-1132 | $-340 | 49.2 | losing for real |

Sorted by Train P&L. A strategy is only interesting if it is ALSO positive in Test and beats coinflip. With ~18 strategies, one or two will look good by pure luck.

Big caveat: real Polymarket prices move with BTC, so the 51c assumption is generous when a move is obvious. The live paper bot uses real Polymarket prices -- trust it over this.
