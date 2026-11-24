# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1261 windows, 34073 settled trades, 397 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1631 | 38.5 | 39.2 | $-879.12 | -5.4% | $120.88 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3416 | 50.7 | 50.3 | $-1148.88 | -3.4% | $-148.88 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2861 | 49.6 | 49.4 | $-1255.07 | -4.4% | $-255.07 | -2.3 | done | losing for real |
| value_ev5 | 2465 | 40.3 | 41.1 | $-1338.57 | -5.4% | $-338.57 | -2.3 | done | losing for real |
| trend_filter | 2019 | 49.0 | 50.4 | $-1603.21 | -7.9% | $-603.21 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2861 | 50.4 | 51.1 | $-1730.62 | -6.0% | $-730.62 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3416 | 49.3 | 50.2 | $-2064.49 | -6.0% | $-1064.49 | -3.6 | done | losing for real |
| coinflip | 4913 | 50.1 | 50.1 | $-2180.40 | -4.4% | $-1180.40 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4913 | 50.4 | 51.4 | $-2827.68 | -5.8% | $-1827.68 | -4.2 | done | losing for real |
| always_up | 4913 | 47.9 | 49.4 | $-3614.74 | -7.4% | $-2614.74 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8065 | 48.0 | 48.9 | $-4718.95 |
| ETH | 8698 | 48.2 | 48.3 | $-4863.75 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
