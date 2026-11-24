# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1253 windows, 33947 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1626 | 38.4 | 39.2 | $-900.17 | -5.5% | $99.83 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3403 | 50.7 | 50.3 | $-1142.03 | -3.4% | $-142.03 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2847 | 49.6 | 49.4 | $-1280.55 | -4.5% | $-280.55 | -2.4 | done | losing for real |
| value_ev5 | 2458 | 40.3 | 41.1 | $-1339.62 | -5.5% | $-339.62 | -2.3 | done | losing for real |
| trend_filter | 2010 | 48.9 | 50.4 | $-1658.69 | -8.3% | $-658.69 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2847 | 50.4 | 51.1 | $-1713.74 | -6.0% | $-713.74 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3403 | 49.3 | 50.2 | $-2078.61 | -6.1% | $-1078.61 | -3.6 | done | losing for real |
| coinflip | 4896 | 50.0 | 50.1 | $-2218.11 | -4.5% | $-1218.11 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4896 | 50.4 | 51.4 | $-2886.29 | -5.9% | $-1886.29 | -4.3 | done | losing for real |
| always_up | 4896 | 47.8 | 49.3 | $-3667.12 | -7.5% | $-2667.12 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8001 | 48.0 | 48.9 | $-4771.59 |
| ETH | 8636 | 48.1 | 48.3 | $-5053.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
