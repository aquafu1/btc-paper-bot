# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1281 windows, 34368 settled trades, 401 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 675 | 33.9 | 35.3 | $-560.36 | -8.3% | $439.64 | -1.6 | done | can't tell from luck |
| value_ev10 | 1651 | 38.5 | 39.2 | $-870.65 | -5.3% | $129.35 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3447 | 50.7 | 50.2 | $-1178.84 | -3.4% | $-178.84 | -2.0 | done | losing for real |
| value_ev5 | 2494 | 40.4 | 41.1 | $-1322.01 | -5.3% | $-322.01 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2881 | 49.5 | 49.4 | $-1349.08 | -4.7% | $-349.08 | -2.5 | done | losing for real |
| trend_filter | 2033 | 49.0 | 50.5 | $-1623.73 | -8.0% | $-623.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2881 | 50.5 | 51.0 | $-1657.81 | -5.8% | $-657.81 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3447 | 49.3 | 50.2 | $-2078.38 | -6.0% | $-1078.38 | -3.6 | done | losing for real |
| coinflip | 4953 | 49.9 | 50.1 | $-2315.37 | -4.7% | $-1315.37 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4953 | 50.5 | 51.4 | $-2780.10 | -5.6% | $-1780.10 | -4.1 | done | losing for real |
| always_up | 4953 | 47.8 | 49.3 | $-3654.51 | -7.4% | $-2654.51 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8208 | 48.0 | 48.8 | $-4940.18 |
| ETH | 8850 | 48.2 | 48.2 | $-4866.44 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
