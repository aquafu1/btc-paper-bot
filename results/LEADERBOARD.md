# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 445 windows, 12236 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 226 | 34.5 | 36.0 | $-169.66 | -7.5% | $830.34 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1043 | 51.2 | 50.0 | $-196.99 | -1.9% | $803.01 | -0.6 | done | can't tell from luck |
| trend_filter | 705 | 50.2 | 50.7 | $-355.52 | -5.0% | $644.48 | -1.4 | done | can't tell from luck |
| value_ev10 | 577 | 38.5 | 40.1 | $-435.06 | -7.5% | $564.94 | -1.5 | done | can't tell from luck |
| value_ev5 | 856 | 40.9 | 41.8 | $-519.74 | -6.1% | $480.26 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1235 | 49.7 | 50.0 | $-529.53 | -4.3% | $470.47 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1235 | 50.3 | 51.6 | $-849.66 | -6.9% | $150.34 | -2.5 | done | losing for real |
| coinflip | 1772 | 50.0 | 50.8 | $-958.56 | -5.4% | $41.44 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1043 | 48.8 | 51.7 | $-1033.20 | -9.9% | $-33.20 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1772 | 49.7 | 51.6 | $-1294.63 | -7.3% | $-294.63 | -3.2 | done | losing for real |
| always_up | 1772 | 45.8 | 50.5 | $-2319.64 | -13.1% | $-1319.64 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2764 | 47.5 | 49.3 | $-2198.29 |
| ETH | 3074 | 47.9 | 48.8 | $-2080.85 |
| SOL | 3180 | 47.6 | 49.3 | $-2562.16 |
| XRP | 3218 | 48.5 | 49.2 | $-1820.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
