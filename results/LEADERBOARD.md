# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 468 windows, 12853 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1088 | 50.7 | 49.9 | $-283.81 | -2.6% | $716.19 | -0.9 | done | can't tell from luck |
| value_ev10 | 607 | 39.0 | 40.1 | $-363.06 | -6.0% | $636.94 | -1.2 | done | can't tell from luck |
| trend_filter | 744 | 49.6 | 50.7 | $-455.59 | -6.1% | $544.41 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1295 | 49.9 | 50.0 | $-488.91 | -3.8% | $511.09 | -1.4 | done | can't tell from luck |
| value_ev5 | 898 | 41.0 | 41.8 | $-495.95 | -5.5% | $504.05 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1295 | 50.1 | 51.6 | $-928.02 | -7.2% | $71.98 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1088 | 49.3 | 51.8 | $-1000.82 | -9.2% | $-0.82 | -3.2 | done | losing for real |
| coinflip | 1867 | 49.9 | 50.8 | $-1037.11 | -5.6% | $-37.11 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1867 | 49.8 | 51.6 | $-1329.07 | -7.1% | $-329.07 | -3.2 | done | losing for real |
| always_up | 1867 | 46.4 | 50.4 | $-2142.44 | -11.5% | $-1142.44 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2905 | 47.6 | 49.3 | $-2226.85 |
| ETH | 3227 | 48.0 | 48.8 | $-2132.14 |
| SOL | 3349 | 47.8 | 49.3 | $-2557.24 |
| XRP | 3372 | 48.5 | 49.1 | $-1744.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
