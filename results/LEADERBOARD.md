# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 808 windows, 22207 settled trades, 21 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 412 | 33.5 | 35.0 | $-331.28 | -8.0% | $668.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1016 | 37.8 | 39.2 | $-694.51 | -6.8% | $305.49 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1861 | 50.1 | 49.6 | $-726.58 | -3.9% | $273.42 | -1.7 | done | can't tell from luck |
| trend_filter | 1299 | 50.2 | 50.9 | $-781.06 | -6.0% | $218.94 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2269 | 50.9 | 50.6 | $-822.42 | -3.6% | $177.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1536 | 40.0 | 41.1 | $-916.63 | -6.0% | $83.37 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1861 | 49.9 | 51.2 | $-1330.88 | -7.2% | $-330.88 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3228 | 51.3 | 51.6 | $-1355.25 | -4.2% | $-355.25 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2269 | 49.1 | 50.2 | $-1368.55 | -6.0% | $-368.55 | -2.9 | done | losing for real |
| coinflip | 3228 | 50.2 | 50.3 | $-1397.47 | -4.3% | $-397.47 | -2.5 | done | losing for real |
| always_up | 3228 | 47.5 | 49.7 | $-2771.12 | -8.6% | $-1771.12 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5042 | 48.4 | 49.1 | $-2811.81 |
| ETH | 5528 | 48.2 | 48.5 | $-3495.53 |
| SOL | 5786 | 48.3 | 48.6 | $-3238.60 |
| XRP | 5851 | 48.5 | 48.5 | $-2949.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
