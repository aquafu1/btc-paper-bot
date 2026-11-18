# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 668 windows, 18467 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 345 | 34.5 | 35.3 | $-215.88 | -6.3% | $784.12 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1570 | 50.4 | 49.6 | $-410.81 | -2.6% | $589.19 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1894 | 51.5 | 50.9 | $-529.89 | -2.8% | $470.11 | -1.2 | done | can't tell from luck |
| value_ev10 | 848 | 38.4 | 39.4 | $-531.27 | -6.3% | $468.73 | -1.5 | done | can't tell from luck |
| trend_filter | 1074 | 50.4 | 50.9 | $-554.47 | -5.2% | $445.53 | -1.7 | done | can't tell from luck |
| value_ev5 | 1280 | 40.8 | 41.3 | $-646.63 | -5.1% | $353.37 | -1.5 | done | can't tell from luck |
| coinflip | 2664 | 50.1 | 50.4 | $-1172.64 | -4.4% | $-172.64 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1570 | 49.6 | 51.3 | $-1235.32 | -7.9% | $-235.32 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1894 | 48.5 | 50.0 | $-1305.29 | -6.9% | $-305.29 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2664 | 50.8 | 51.8 | $-1417.13 | -5.3% | $-417.13 | -2.8 | done | losing for real |
| always_up | 2664 | 47.5 | 49.8 | $-2262.83 | -8.5% | $-1262.83 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4200 | 48.3 | 49.2 | $-2453.40 |
| ETH | 4606 | 48.3 | 48.6 | $-2755.11 |
| SOL | 4808 | 48.2 | 48.8 | $-2797.83 |
| XRP | 4853 | 48.6 | 48.6 | $-2275.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
