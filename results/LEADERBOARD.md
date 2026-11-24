# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1265 windows, 34139 settled trades, 389 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 666 | 34.1 | 35.3 | $-534.16 | -8.0% | $465.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1634 | 38.4 | 39.2 | $-909.12 | -5.6% | $90.88 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3424 | 50.7 | 50.2 | $-1170.75 | -3.4% | $-170.75 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2866 | 49.6 | 49.4 | $-1274.67 | -4.4% | $-274.67 | -2.4 | done | losing for real |
| value_ev5 | 2471 | 40.3 | 41.1 | $-1380.15 | -5.6% | $-380.15 | -2.4 | done | losing for real |
| trend_filter | 2025 | 49.0 | 50.4 | $-1618.74 | -8.0% | $-618.74 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2866 | 50.4 | 51.1 | $-1723.87 | -6.0% | $-723.87 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3424 | 49.3 | 50.2 | $-2064.60 | -6.0% | $-1064.60 | -3.6 | done | losing for real |
| coinflip | 4921 | 50.0 | 50.1 | $-2237.86 | -4.5% | $-1237.86 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4921 | 50.4 | 51.4 | $-2848.95 | -5.8% | $-1848.95 | -4.2 | done | losing for real |
| always_up | 4921 | 47.9 | 49.4 | $-3613.46 | -7.3% | $-2613.46 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8096 | 48.0 | 48.9 | $-4832.28 |
| ETH | 8733 | 48.2 | 48.3 | $-4959.81 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
