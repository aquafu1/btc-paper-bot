# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1115 windows, 30838 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 589 | 34.6 | 35.1 | $-339.77 | -5.8% | $660.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3110 | 51.2 | 50.5 | $-785.25 | -2.5% | $214.75 | -1.4 | done | can't tell from luck |
| value_ev10 | 1437 | 38.0 | 39.1 | $-906.08 | -6.3% | $93.92 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2616 | 49.7 | 49.4 | $-1085.67 | -4.2% | $-85.67 | -2.1 | done | losing for real |
| value_ev5 | 2177 | 40.0 | 41.0 | $-1280.38 | -5.9% | $-280.38 | -2.3 | done | losing for real |
| trend_filter | 1827 | 49.2 | 50.4 | $-1378.65 | -7.5% | $-378.65 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2616 | 50.3 | 51.1 | $-1683.70 | -6.4% | $-683.70 | -3.4 | done | losing for real |
| coinflip | 4452 | 50.4 | 50.2 | $-1750.63 | -3.9% | $-750.63 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3110 | 48.8 | 50.2 | $-2118.69 | -6.8% | $-1118.69 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4452 | 50.5 | 51.4 | $-2483.36 | -5.6% | $-1483.36 | -3.8 | done | losing for real |
| always_up | 4452 | 47.6 | 49.3 | $-3471.16 | -7.8% | $-2471.16 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7060 | 48.4 | 49.0 | $-3571.01 |
| ETH | 7639 | 48.1 | 48.4 | $-4690.13 |
| SOL | 8025 | 48.1 | 48.4 | $-4471.21 |
| XRP | 8114 | 48.2 | 48.2 | $-4551.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
