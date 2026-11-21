# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 977 windows, 27135 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 500 | 34.6 | 34.9 | $-235.26 | -4.7% | $764.74 | -0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2772 | 51.2 | 50.5 | $-754.76 | -2.7% | $245.24 | -1.4 | done | can't tell from luck |
| value_ev10 | 1239 | 37.9 | 39.1 | $-774.46 | -6.3% | $225.54 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2321 | 50.1 | 49.7 | $-924.19 | -4.0% | $75.81 | -1.9 | done | can't tell from luck |
| value_ev5 | 1878 | 39.8 | 41.0 | $-1111.80 | -5.9% | $-111.80 | -2.2 | done | losing for real |
| trend_filter | 1626 | 49.7 | 50.9 | $-1161.11 | -7.1% | $-161.11 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2321 | 49.9 | 50.9 | $-1630.75 | -7.0% | $-630.75 | -3.5 | done | losing for real |
| coinflip | 3902 | 50.2 | 50.3 | $-1796.90 | -4.6% | $-796.90 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2772 | 48.8 | 50.3 | $-1959.76 | -7.1% | $-959.76 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3902 | 50.7 | 51.5 | $-2106.08 | -5.4% | $-1106.08 | -3.5 | done | losing for real |
| always_up | 3902 | 46.7 | 49.6 | $-3949.99 | -10.1% | $-2949.99 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6188 | 48.2 | 49.1 | $-3522.11 |
| ETH | 6750 | 48.0 | 48.5 | $-4339.06 |
| SOL | 7083 | 48.1 | 48.6 | $-4122.68 |
| XRP | 7114 | 48.1 | 48.4 | $-4421.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
