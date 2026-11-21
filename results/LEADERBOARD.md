# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 978 windows, 27151 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 500 | 34.6 | 34.9 | $-235.26 | -4.7% | $764.74 | -0.8 | done | can't tell from luck |
| value_ev10 | 1241 | 38.0 | 39.1 | $-747.53 | -6.0% | $252.47 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2772 | 51.2 | 50.5 | $-754.76 | -2.7% | $245.24 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2323 | 50.2 | 49.7 | $-897.26 | -3.9% | $102.74 | -1.9 | done | can't tell from luck |
| value_ev5 | 1880 | 39.9 | 41.0 | $-1084.87 | -5.8% | $-84.87 | -2.1 | done | losing for real |
| trend_filter | 1628 | 49.8 | 50.9 | $-1134.18 | -7.0% | $-134.18 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2323 | 49.8 | 50.9 | $-1650.75 | -7.1% | $-650.75 | -3.5 | done | losing for real |
| coinflip | 3904 | 50.2 | 50.3 | $-1769.97 | -4.5% | $-769.97 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2772 | 48.8 | 50.3 | $-1959.76 | -7.1% | $-959.76 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3904 | 50.8 | 51.5 | $-2079.15 | -5.3% | $-1079.15 | -3.4 | done | losing for real |
| always_up | 3904 | 46.7 | 49.6 | $-3969.99 | -10.2% | $-2969.99 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6188 | 48.2 | 49.1 | $-3522.11 |
| ETH | 6750 | 48.0 | 48.5 | $-4339.06 |
| SOL | 7091 | 48.1 | 48.6 | $-4063.12 |
| XRP | 7122 | 48.2 | 48.4 | $-4359.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
