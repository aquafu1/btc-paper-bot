# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1083 windows, 29947 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 563 | 34.5 | 35.2 | $-338.28 | -6.0% | $661.72 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3028 | 51.2 | 50.5 | $-820.27 | -2.7% | $179.73 | -1.5 | done | can't tell from luck |
| value_ev10 | 1385 | 37.8 | 39.2 | $-940.65 | -6.8% | $59.35 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2541 | 49.8 | 49.6 | $-1089.15 | -4.3% | $-89.15 | -2.2 | done | losing for real |
| trend_filter | 1781 | 49.6 | 50.6 | $-1217.27 | -6.8% | $-217.27 | -3.0 | done | losing for real |
| value_ev5 | 2105 | 39.8 | 41.1 | $-1334.13 | -6.3% | $-334.13 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2541 | 50.2 | 51.1 | $-1665.87 | -6.6% | $-665.87 | -3.4 | done | losing for real |
| coinflip | 4325 | 50.5 | 50.3 | $-1687.65 | -3.9% | $-687.65 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4325 | 51.1 | 51.5 | $-2013.10 | -4.7% | $-1013.10 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3028 | 48.8 | 50.3 | $-2087.41 | -6.9% | $-1087.41 | -3.8 | done | losing for real |
| always_up | 4325 | 47.4 | 49.4 | $-3603.66 | -8.3% | $-2603.66 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6841 | 48.5 | 49.0 | $-3319.66 |
| ETH | 7414 | 48.2 | 48.5 | $-4467.11 |
| SOL | 7811 | 48.1 | 48.5 | $-4401.67 |
| XRP | 7881 | 48.3 | 48.3 | $-4609.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
