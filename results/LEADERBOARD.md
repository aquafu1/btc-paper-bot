# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1146 windows, 31662 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 610 | 34.4 | 35.2 | $-412.50 | -6.8% | $587.50 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 3180 | 50.9 | 50.4 | $-994.70 | -3.1% | $5.30 | -1.8 | done | can't tell from luck |
| value_ev10 | 1489 | 37.9 | 39.2 | $-1001.54 | -6.7% | $-1.54 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2674 | 49.7 | 49.5 | $-1156.98 | -4.3% | $-156.98 | -2.2 | done | losing for real |
| value_ev5 | 2249 | 40.0 | 41.1 | $-1372.64 | -6.1% | $-372.64 | -2.5 | done | losing for real |
| trend_filter | 1878 | 49.0 | 50.5 | $-1506.54 | -8.0% | $-506.54 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2674 | 50.3 | 51.1 | $-1679.85 | -6.3% | $-679.85 | -3.3 | done | losing for real |
| coinflip | 4576 | 50.3 | 50.2 | $-1907.43 | -4.2% | $-907.43 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3180 | 49.1 | 50.2 | $-1972.88 | -6.2% | $-972.88 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4576 | 50.2 | 51.4 | $-2892.89 | -6.3% | $-1892.89 | -4.4 | done | losing for real |
| always_up | 4576 | 47.9 | 49.4 | $-3335.86 | -7.3% | $-2335.86 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7256 | 48.2 | 49.0 | $-3853.48 |
| ETH | 7843 | 48.1 | 48.4 | $-4707.72 |
| SOL | 8244 | 48.1 | 48.4 | $-4644.49 |
| XRP | 8319 | 48.1 | 48.2 | $-5028.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
