# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 714 windows, 19682 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 376 | 33.8 | 34.8 | $-284.03 | -7.6% | $715.97 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2015 | 51.6 | 50.8 | $-511.48 | -2.5% | $488.52 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1655 | 50.2 | 49.5 | $-521.66 | -3.2% | $478.34 | -1.3 | done | can't tell from luck |
| value_ev10 | 906 | 38.2 | 39.0 | $-552.57 | -6.1% | $447.43 | -1.5 | done | can't tell from luck |
| value_ev5 | 1364 | 40.8 | 41.0 | $-625.69 | -4.6% | $374.31 | -1.4 | done | can't tell from luck |
| trend_filter | 1152 | 50.3 | 50.9 | $-634.74 | -5.5% | $365.26 | -1.9 | done | can't tell from luck |
| coinflip | 2848 | 50.2 | 50.3 | $-1207.94 | -4.2% | $-207.94 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1655 | 49.8 | 51.3 | $-1258.26 | -7.6% | $-258.26 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2848 | 51.1 | 51.8 | $-1419.48 | -5.0% | $-419.48 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2015 | 48.4 | 50.0 | $-1427.24 | -7.1% | $-427.24 | -3.2 | done | losing for real |
| always_up | 2848 | 47.3 | 49.5 | $-2435.08 | -8.6% | $-1435.08 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4460 | 48.1 | 49.0 | $-2720.63 |
| ETH | 4898 | 48.3 | 48.5 | $-2828.59 |
| SOL | 5133 | 48.2 | 48.7 | $-2929.33 |
| XRP | 5191 | 48.6 | 48.4 | $-2399.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
