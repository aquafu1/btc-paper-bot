# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1152 windows, 31819 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 613 | 34.6 | 35.2 | $-387.85 | -6.3% | $612.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1502 | 38.3 | 39.2 | $-851.63 | -5.7% | $148.37 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3195 | 50.9 | 50.4 | $-987.24 | -3.1% | $12.76 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2682 | 49.7 | 49.5 | $-1183.76 | -4.4% | $-183.76 | -2.3 | done | losing for real |
| value_ev5 | 2266 | 40.3 | 41.1 | $-1189.73 | -5.3% | $-189.73 | -2.1 | done | losing for real |
| trend_filter | 1884 | 48.9 | 50.5 | $-1542.30 | -8.2% | $-542.30 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2682 | 50.3 | 51.0 | $-1656.85 | -6.2% | $-656.85 | -3.3 | done | losing for real |
| coinflip | 4600 | 50.3 | 50.2 | $-1883.14 | -4.1% | $-883.14 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3195 | 49.1 | 50.2 | $-1973.20 | -6.2% | $-973.20 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4600 | 50.1 | 51.4 | $-2934.61 | -6.4% | $-1934.61 | -4.5 | done | losing for real |
| always_up | 4600 | 47.8 | 49.4 | $-3423.43 | -7.4% | $-2423.43 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7289 | 48.3 | 49.0 | $-3739.54 |
| ETH | 7883 | 48.1 | 48.4 | $-4641.95 |
| SOL | 8283 | 48.1 | 48.4 | $-4578.51 |
| XRP | 8364 | 48.1 | 48.2 | $-5053.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
