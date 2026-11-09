# Backtest report (FAKE money)

Data: Coinbase BTC-USD 1-min candles, Oct 19 16:55 UTC to Nov 09 17:55 UTC (21 days).
Assumed entry price 0.51, fee 1.5% of stake, $10 per trade. Break-even win rate = 51.8%.

**Train** = first 14 days (where you'd pick a strategy). **Test** = last 7 days (did it still work on data it wasn't picked on?).

| Strategy | Trades | Win % | P&L (all) | Train P&L | Test P&L | Test win % | Verdict |
|---|---|---|---|---|---|---|---|
| reversal_5m_0.10pct | 434 | 52.8 | $+85 | $+155 | $-70 | 49.7 | can't tell from luck |
| reversal_5m_0.00pct | 2015 | 52.0 | $+77 | $+143 | $-66 | 51.3 | can't tell from luck |
| momentum_15m_0.30pct | 163 | 46.6 | $-164 | $+66 | $-230 | 35.2 | can't tell from luck |
| reversal_5m_0.30pct | 35 | 54.3 | $+17 | $+44 | $-27 | 45.0 | too few trades |
| reversal_15m_0.10pct | 835 | 52.2 | $+74 | $+38 | $+36 | 52.4 | can't tell from luck |
| momentum_60m_0.30pct | 521 | 48.4 | $-347 | $+33 | $-379 | 41.6 | can't tell from luck |
| momentum_5m_0.30pct | 35 | 45.7 | $-42 | $-54 | $+13 | 55.0 | too few trades |
| reversal_15m_0.30pct | 163 | 53.4 | $+51 | $-130 | $+181 | 64.8 | can't tell from luck |
| reversal_60m_0.10pct | 1364 | 52.3 | $+136 | $-218 | $+353 | 55.8 | can't tell from luck |
| trend_filter | 527 | 45.7 | $-624 | $-249 | $-375 | 40.9 | losing for real |
| reversal_60m_0.30pct | 521 | 51.6 | $-14 | $-262 | $+248 | 58.4 | can't tell from luck |
| reversal_15m_0.00pct | 2015 | 51.5 | $-119 | $-269 | $+150 | 52.9 | can't tell from luck |
| reversal_60m_0.00pct | 2015 | 51.7 | $-40 | $-308 | $+268 | 53.8 | can't tell from luck |
| momentum_5m_0.10pct | 434 | 47.2 | $-385 | $-335 | $-51 | 50.3 | can't tell from luck |
| momentum_15m_0.10pct | 835 | 47.8 | $-652 | $-413 | $-239 | 47.6 | losing for real |
| momentum_60m_0.10pct | 1364 | 47.7 | $-1080 | $-414 | $-666 | 44.2 | losing for real |
| coinflip | 2015 | 50.1 | $-648 | $-524 | $-124 | 50.8 | can't tell from luck |
| momentum_60m_0.00pct | 2015 | 48.3 | $-1354 | $-622 | $-732 | 46.2 | losing for real |
| momentum_15m_0.00pct | 2015 | 48.5 | $-1276 | $-661 | $-615 | 47.1 | losing for real |
| momentum_5m_0.00pct | 2015 | 48.0 | $-1472 | $-1073 | $-399 | 48.7 | losing for real |
| always_up | 2015 | 48.0 | $-1472 | $-1112 | $-360 | 49.0 | losing for real |

Sorted by Train P&L. A strategy is only interesting if it is ALSO positive in Test and beats coinflip. With ~18 strategies, one or two will look good by pure luck.

Big caveat: real Polymarket prices move with BTC, so the 51c assumption is generous when a move is obvious. The live paper bot uses real Polymarket prices -- trust it over this.
