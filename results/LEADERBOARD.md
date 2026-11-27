# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1592 windows, 38632 settled trades, 405 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 813 | 34.6 | 35.1 | $-565.00 | -6.9% | $435.00 | -1.5 | done | can't tell from luck |
| value_ev10 | 1921 | 38.5 | 39.0 | $-989.67 | -5.2% | $10.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3814 | 50.9 | 50.0 | $-993.04 | -2.6% | $6.96 | -1.6 | done | can't tell from luck |
| value_ev5 | 2884 | 40.5 | 41.0 | $-1430.38 | -5.0% | $-430.38 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3195 | 51.0 | 50.9 | $-1484.58 | -4.6% | $-484.58 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3195 | 49.0 | 49.2 | $-1705.71 | -5.3% | $-705.71 | -3.0 | done | losing for real |
| trend_filter | 2271 | 48.5 | 50.3 | $-2016.82 | -8.9% | $-1016.82 | -4.3 | done | losing for real |
| coinflip | 5575 | 50.1 | 49.9 | $-2258.56 | -4.1% | $-1258.56 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3814 | 49.1 | 50.2 | $-2362.65 | -6.2% | $-1362.65 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5575 | 50.1 | 51.3 | $-3507.69 | -6.3% | $-2507.69 | -4.8 | done | losing for real |
| always_up | 5575 | 48.2 | 49.1 | $-3546.52 | -6.4% | $-2546.52 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10249 | 48.0 | 48.6 | $-5692.57 |
| ETH | 11073 | 48.0 | 47.7 | $-5583.83 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
