# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 915 windows, 25287 settled trades, 21 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 473 | 34.9 | 34.8 | $-191.30 | -4.0% | $808.70 | -0.7 | done | can't tell from luck |
| value_ev10 | 1157 | 38.0 | 39.1 | $-678.14 | -5.9% | $321.86 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2145 | 50.0 | 49.8 | $-952.27 | -4.4% | $47.73 | -2.1 | done | losing for real |
| trend_filter | 1503 | 50.0 | 51.0 | $-1005.56 | -6.7% | $-5.56 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2572 | 50.5 | 50.5 | $-1086.60 | -4.2% | $-86.60 | -2.1 | done | losing for real |
| value_ev5 | 1752 | 39.6 | 41.0 | $-1142.52 | -6.5% | $-142.52 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2572 | 49.5 | 50.3 | $-1393.51 | -5.4% | $-393.51 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2145 | 50.0 | 50.9 | $-1449.26 | -6.8% | $-449.26 | -3.2 | done | losing for real |
| coinflip | 3656 | 50.3 | 50.3 | $-1574.16 | -4.3% | $-574.16 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3656 | 51.1 | 51.6 | $-1718.17 | -4.7% | $-718.17 | -2.9 | done | losing for real |
| always_up | 3656 | 46.8 | 49.6 | $-3666.72 | -10.0% | $-2666.72 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5759 | 48.2 | 49.0 | $-3309.61 |
| ETH | 6288 | 48.2 | 48.5 | $-3930.61 |
| SOL | 6597 | 48.2 | 48.6 | $-3865.44 |
| XRP | 6643 | 48.3 | 48.5 | $-3752.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
