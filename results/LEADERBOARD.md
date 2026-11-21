# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 999 windows, 27765 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 513 | 34.3 | 35.0 | $-286.26 | -5.6% | $713.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2831 | 51.1 | 50.4 | $-831.44 | -2.9% | $168.56 | -1.6 | done | can't tell from luck |
| value_ev10 | 1272 | 37.6 | 39.1 | $-879.88 | -6.9% | $120.12 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2383 | 49.8 | 49.7 | $-1102.43 | -4.6% | $-102.43 | -2.3 | done | losing for real |
| value_ev5 | 1926 | 39.6 | 41.0 | $-1240.43 | -6.4% | $-240.43 | -2.4 | done | losing for real |
| trend_filter | 1662 | 49.5 | 50.8 | $-1247.80 | -7.5% | $-247.80 | -3.1 | done | losing for real |
| reversal_60m_0.30pct | 2383 | 50.2 | 51.0 | $-1543.97 | -6.5% | $-543.97 | -3.2 | done | losing for real |
| coinflip | 3988 | 50.3 | 50.3 | $-1767.26 | -4.4% | $-767.26 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2831 | 48.9 | 50.3 | $-1950.37 | -6.9% | $-950.37 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3988 | 50.7 | 51.5 | $-2235.95 | -5.6% | $-1235.95 | -3.7 | done | losing for real |
| always_up | 3988 | 46.9 | 49.5 | $-3866.02 | -9.7% | $-2866.02 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6327 | 48.2 | 49.0 | $-3605.72 |
| ETH | 6899 | 48.0 | 48.5 | $-4551.03 |
| SOL | 7260 | 48.1 | 48.5 | $-4161.65 |
| XRP | 7279 | 48.1 | 48.4 | $-4633.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
