# Backtest report (FAKE money)

Data: Coinbase BTC-USD 1-min candles, Oct 20 20:04 UTC to Nov 10 21:04 UTC (21 days).
Assumed entry price 0.51, Polymarket's crypto taker fee (0.07 x p x (1-p) per share), $10 per trade. Break-even win rate = 52.8%.

**Train** = first 14 days (where you'd pick a strategy). **Test** = last 7 days (did it still work on data it wasn't picked on?).

| Strategy | Trades | Win % | P&L (all) | Train P&L | Test P&L | Test win % | Verdict |
|---|---|---|---|---|---|---|---|
| momentum_15m_0.30pct | 167 | 46.7 | $-193 | $+54 | $-247 | 34.7 | can't tell from luck |
| reversal_5m_0.30pct | 35 | 51.4 | $-9 | $+30 | $-40 | 42.9 | too few trades (35/100) |
| reversal_5m_0.10pct | 455 | 51.6 | $-100 | $-7 | $-94 | 50.0 | can't tell from luck |
| momentum_5m_0.30pct | 35 | 48.6 | $-28 | $-45 | $+17 | 57.1 | too few trades (35/100) |
| momentum_60m_0.30pct | 536 | 47.8 | $-513 | $-54 | $-458 | 40.9 | losing for real |
| reversal_15m_0.10pct | 851 | 52.9 | $+11 | $-70 | $+81 | 54.2 | can't tell from luck |
| reversal_5m_0.00pct | 2015 | 52.5 | $-116 | $-110 | $-7 | 52.8 | can't tell from luck |
| reversal_15m_0.30pct | 167 | 53.3 | $+15 | $-155 | $+170 | 65.3 | can't tell from luck |
| momentum_5m_0.10pct | 455 | 48.4 | $-384 | $-291 | $-94 | 50.0 | can't tell from luck |
| reversal_60m_0.30pct | 536 | 52.2 | $-58 | $-300 | $+242 | 59.1 | can't tell from luck |
| reversal_60m_0.10pct | 1378 | 52.5 | $-90 | $-335 | $+245 | 55.6 | can't tell from luck |
| trend_filter | 538 | 45.2 | $-779 | $-341 | $-438 | 40.1 | losing for real |
| reversal_15m_0.00pct | 2015 | 51.9 | $-363 | $-469 | $+107 | 53.7 | can't tell from luck |
| coinflip | 2015 | 49.4 | $-1309 | $-488 | $-821 | 46.3 | losing for real |
| momentum_15m_0.10pct | 851 | 47.1 | $-917 | $-506 | $-411 | 45.8 | losing for real |
| reversal_60m_0.00pct | 2015 | 51.8 | $-400 | $-564 | $+164 | 54.1 | can't tell from luck |
| momentum_60m_0.10pct | 1378 | 47.5 | $-1377 | $-638 | $-739 | 44.4 | losing for real |
| momentum_60m_0.00pct | 2015 | 48.2 | $-1745 | $-867 | $-878 | 45.9 | losing for real |
| momentum_15m_0.00pct | 2015 | 48.1 | $-1783 | $-962 | $-821 | 46.3 | losing for real |
| momentum_5m_0.00pct | 2015 | 47.5 | $-2029 | $-1321 | $-708 | 47.2 | losing for real |
| always_up | 2015 | 48.0 | $-1840 | $-1359 | $-480 | 49.0 | losing for real |

Sorted by Train P&L. A strategy is only interesting if it is ALSO positive in Test and beats coinflip. With ~18 strategies, one or two will look good by pure luck.

Big caveat: real Polymarket prices move with BTC, so the 51c assumption is generous when a move is obvious. The live paper bot uses real Polymarket prices -- trust it over this.
