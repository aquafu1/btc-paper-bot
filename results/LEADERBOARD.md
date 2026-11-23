# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1145 windows, 31643 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 610 | 34.4 | 35.2 | $-412.50 | -6.8% | $587.50 | -1.3 | done | can't tell from luck |
| value_ev10 | 1487 | 38.0 | 39.2 | $-981.54 | -6.6% | $18.46 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 3179 | 50.9 | 50.4 | $-984.70 | -3.1% | $15.30 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2672 | 49.7 | 49.5 | $-1153.86 | -4.3% | $-153.86 | -2.2 | done | losing for real |
| value_ev5 | 2247 | 40.0 | 41.1 | $-1352.64 | -6.0% | $-352.64 | -2.4 | done | losing for real |
| trend_filter | 1878 | 49.0 | 50.5 | $-1506.54 | -8.0% | $-506.54 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2672 | 50.3 | 51.1 | $-1679.37 | -6.3% | $-679.37 | -3.3 | done | losing for real |
| coinflip | 4573 | 50.3 | 50.2 | $-1877.43 | -4.1% | $-877.43 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3179 | 49.1 | 50.2 | $-1979.76 | -6.2% | $-979.76 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4573 | 50.2 | 51.4 | $-2882.40 | -6.3% | $-1882.40 | -4.4 | done | losing for real |
| always_up | 4573 | 47.9 | 49.4 | $-3339.91 | -7.3% | $-2339.91 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7256 | 48.2 | 49.0 | $-3853.48 |
| ETH | 7838 | 48.2 | 48.4 | $-4674.88 |
| SOL | 8235 | 48.1 | 48.4 | $-4605.13 |
| XRP | 8314 | 48.1 | 48.2 | $-5017.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
