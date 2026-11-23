# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1147 windows, 31686 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 610 | 34.4 | 35.2 | $-412.50 | -6.8% | $587.50 | -1.3 | done | can't tell from luck |
| value_ev10 | 1490 | 38.0 | 39.2 | $-991.04 | -6.7% | $8.96 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 3180 | 50.9 | 50.4 | $-994.70 | -3.1% | $5.30 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2677 | 49.6 | 49.5 | $-1186.98 | -4.4% | $-186.98 | -2.3 | done | losing for real |
| value_ev5 | 2251 | 40.0 | 41.1 | $-1352.13 | -6.0% | $-352.13 | -2.4 | done | losing for real |
| trend_filter | 1881 | 48.9 | 50.5 | $-1536.54 | -8.2% | $-536.54 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2677 | 50.4 | 51.1 | $-1650.58 | -6.2% | $-650.58 | -3.3 | done | losing for real |
| coinflip | 4580 | 50.3 | 50.2 | $-1909.37 | -4.2% | $-909.37 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3180 | 49.1 | 50.2 | $-1972.88 | -6.2% | $-972.88 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4580 | 50.2 | 51.4 | $-2932.89 | -6.4% | $-1932.89 | -4.5 | done | losing for real |
| always_up | 4580 | 47.9 | 49.4 | $-3375.86 | -7.4% | $-2375.86 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7262 | 48.2 | 49.0 | $-3894.71 |
| ETH | 7851 | 48.1 | 48.4 | $-4705.69 |
| SOL | 8251 | 48.0 | 48.4 | $-4674.49 |
| XRP | 8322 | 48.1 | 48.2 | $-5040.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
