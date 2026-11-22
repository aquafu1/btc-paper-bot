# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1120 windows, 30994 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 591 | 34.5 | 35.1 | $-359.77 | -6.1% | $640.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3127 | 51.1 | 50.4 | $-833.74 | -2.7% | $166.26 | -1.5 | done | can't tell from luck |
| value_ev10 | 1448 | 38.1 | 39.2 | $-886.97 | -6.1% | $113.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2629 | 49.7 | 49.4 | $-1117.73 | -4.3% | $-117.73 | -2.2 | done | losing for real |
| value_ev5 | 2190 | 40.1 | 41.1 | $-1242.09 | -5.7% | $-242.09 | -2.2 | done | losing for real |
| trend_filter | 1837 | 49.1 | 50.4 | $-1421.61 | -7.7% | $-421.61 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2629 | 50.3 | 51.1 | $-1669.25 | -6.3% | $-669.25 | -3.3 | done | losing for real |
| coinflip | 4472 | 50.4 | 50.2 | $-1776.61 | -4.0% | $-776.61 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3127 | 48.9 | 50.2 | $-2077.57 | -6.6% | $-1077.57 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4472 | 50.4 | 51.4 | $-2591.82 | -5.8% | $-1591.82 | -4.0 | done | losing for real |
| always_up | 4472 | 47.7 | 49.3 | $-3393.86 | -7.6% | $-2393.86 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7104 | 48.4 | 49.0 | $-3609.18 |
| ETH | 7679 | 48.1 | 48.4 | $-4624.45 |
| SOL | 8062 | 48.0 | 48.4 | $-4544.48 |
| XRP | 8149 | 48.2 | 48.2 | $-4592.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
