# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 364 windows, 9830 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 8:45 PM | too few trades (189/200) |
| value_ev10 | 477 | 41.3 | 40.3 | $-42.64 | -0.9% | $957.36 | -0.2 | done | can't tell from luck |
| value_ev5 | 706 | 42.5 | 42.0 | $-168.96 | -2.4% | $831.04 | -0.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 975 | 51.8 | 52.1 | $-441.61 | -4.5% | $558.39 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 807 | 49.2 | 49.7 | $-443.90 | -5.5% | $556.10 | -1.6 | done | can't tell from luck |
| trend_filter | 544 | 48.5 | 50.6 | $-450.34 | -8.3% | $549.66 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 807 | 50.8 | 52.0 | $-497.12 | -6.2% | $502.88 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 975 | 48.2 | 49.6 | $-631.34 | -6.5% | $368.66 | -2.0 | done | losing for real |
| coinflip | 1450 | 50.1 | 50.8 | $-733.69 | -5.1% | $266.31 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1450 | 49.4 | 51.6 | $-1091.89 | -7.5% | $-91.89 | -3.0 | done | losing for real |
| always_up | 1450 | 45.8 | 50.7 | $-1907.41 | -13.2% | $-907.41 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2201 | 47.3 | 49.3 | $-1744.19 |
| ETH | 2476 | 47.7 | 48.8 | $-1701.45 |
| SOL | 2545 | 48.1 | 49.4 | $-1753.12 |
| XRP | 2608 | 48.9 | 49.1 | $-1194.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
