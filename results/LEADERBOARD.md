# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 635 windows, 17558 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1485 | 51.0 | 49.5 | $-206.10 | -1.4% | $793.90 | -0.5 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1016 | 50.3 | 50.8 | $-540.52 | -5.3% | $459.48 | -1.7 | done | can't tell from luck |
| value_ev10 | 807 | 38.4 | 39.5 | $-559.42 | -6.9% | $440.58 | -1.6 | done | can't tell from luck |
| value_ev5 | 1224 | 40.7 | 41.4 | $-708.56 | -5.8% | $291.44 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1806 | 51.1 | 51.1 | $-764.53 | -4.2% | $235.47 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1806 | 48.9 | 50.0 | $-1067.14 | -5.9% | $-67.14 | -2.5 | done | losing for real |
| coinflip | 2533 | 50.1 | 50.5 | $-1189.52 | -4.7% | $-189.52 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1485 | 49.0 | 51.5 | $-1387.85 | -9.3% | $-387.85 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2533 | 50.6 | 51.7 | $-1445.25 | -5.7% | $-445.25 | -3.0 | done | losing for real |
| always_up | 2533 | 47.3 | 49.7 | $-2223.12 | -8.8% | $-1223.12 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3985 | 48.3 | 49.2 | $-2432.51 |
| ETH | 4402 | 48.2 | 48.6 | $-2643.73 |
| SOL | 4555 | 48.0 | 48.8 | $-2974.69 |
| XRP | 4616 | 48.5 | 48.6 | $-2315.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
