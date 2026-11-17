# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 603 windows, 16653 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1408 | 51.0 | 49.6 | $-248.06 | -1.8% | $751.94 | -0.7 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| trend_filter | 960 | 50.0 | 50.9 | $-586.54 | -6.1% | $413.46 | -1.9 | done | can't tell from luck |
| value_ev5 | 1166 | 40.5 | 41.2 | $-675.25 | -5.8% | $324.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1699 | 51.0 | 50.9 | $-722.00 | -4.2% | $278.00 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1699 | 49.0 | 50.0 | $-1024.19 | -6.0% | $-24.19 | -2.5 | done | losing for real |
| coinflip | 2404 | 50.0 | 50.5 | $-1200.36 | -5.0% | $-200.36 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1408 | 49.0 | 51.4 | $-1287.97 | -9.1% | $-287.97 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2404 | 50.2 | 51.8 | $-1584.99 | -6.6% | $-584.99 | -3.4 | done | losing for real |
| always_up | 2404 | 47.2 | 49.8 | $-2220.25 | -9.2% | $-1220.25 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3785 | 48.0 | 49.2 | $-2500.19 |
| ETH | 4153 | 47.9 | 48.6 | $-2732.98 |
| SOL | 4327 | 47.9 | 48.7 | $-2892.23 |
| XRP | 4388 | 48.5 | 48.6 | $-2179.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
