# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1495 windows, 37366 settled trades, 369 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 758 | 34.3 | 35.4 | $-583.02 | -7.7% | $416.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1821 | 38.4 | 39.2 | $-984.96 | -5.4% | $15.04 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3716 | 50.9 | 50.1 | $-1030.19 | -2.8% | $-30.19 | -1.7 | done | can't tell from luck |
| value_ev5 | 2749 | 40.5 | 41.1 | $-1397.22 | -5.1% | $-397.22 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3123 | 51.0 | 51.0 | $-1474.73 | -4.7% | $-474.73 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3123 | 49.0 | 49.2 | $-1659.55 | -5.3% | $-659.55 | -3.0 | done | losing for real |
| trend_filter | 2217 | 48.6 | 50.3 | $-1911.44 | -8.6% | $-911.44 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3716 | 49.1 | 50.2 | $-2245.61 | -6.0% | $-1245.61 | -3.7 | done | losing for real |
| coinflip | 5381 | 50.0 | 50.0 | $-2340.13 | -4.3% | $-1340.13 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5381 | 50.2 | 51.3 | $-3324.51 | -6.2% | $-2324.51 | -4.7 | done | losing for real |
| always_up | 5381 | 48.0 | 49.2 | $-3609.56 | -6.7% | $-2609.56 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9661 | 48.0 | 48.7 | $-5320.47 |
| ETH | 10395 | 48.0 | 47.9 | $-5656.21 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
