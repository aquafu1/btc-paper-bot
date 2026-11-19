# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 767 windows, 21140 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 399 | 33.3 | 34.9 | $-341.45 | -8.6% | $658.55 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2159 | 51.4 | 50.6 | $-551.01 | -2.6% | $448.99 | -1.2 | done | can't tell from luck |
| value_ev10 | 968 | 37.8 | 39.1 | $-661.05 | -6.8% | $338.95 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1785 | 49.9 | 49.5 | $-702.11 | -3.9% | $297.89 | -1.7 | done | can't tell from luck |
| trend_filter | 1244 | 49.8 | 50.8 | $-825.43 | -6.6% | $174.57 | -2.4 | done | losing for real |
| value_ev5 | 1461 | 40.1 | 41.0 | $-867.45 | -5.9% | $132.55 | -1.9 | done | can't tell from luck |
| coinflip | 3060 | 50.4 | 50.2 | $-1189.05 | -3.9% | $-189.05 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1785 | 50.1 | 51.3 | $-1239.78 | -6.9% | $-239.78 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2159 | 48.6 | 50.2 | $-1546.95 | -7.2% | $-546.95 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3060 | 50.9 | 51.7 | $-1579.19 | -5.2% | $-579.19 | -2.9 | done | losing for real |
| always_up | 3060 | 47.0 | 49.6 | $-2861.21 | -9.4% | $-1861.21 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4794 | 48.2 | 49.1 | $-2909.17 |
| ETH | 5278 | 48.0 | 48.5 | $-3508.67 |
| SOL | 5502 | 48.0 | 48.5 | $-3280.30 |
| XRP | 5566 | 48.5 | 48.4 | $-2666.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
