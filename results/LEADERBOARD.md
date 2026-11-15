# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 446 windows, 12258 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 226 | 34.5 | 36.0 | $-169.66 | -7.5% | $830.34 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1044 | 51.2 | 50.0 | $-188.59 | -1.8% | $811.41 | -0.6 | done | can't tell from luck |
| trend_filter | 707 | 50.1 | 50.7 | $-375.52 | -5.3% | $624.48 | -1.4 | done | can't tell from luck |
| value_ev10 | 577 | 38.5 | 40.1 | $-435.06 | -7.5% | $564.94 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1238 | 49.8 | 50.0 | $-503.57 | -4.1% | $496.43 | -1.4 | done | can't tell from luck |
| value_ev5 | 856 | 40.9 | 41.8 | $-519.74 | -6.1% | $480.26 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1238 | 50.2 | 51.6 | $-879.66 | -7.1% | $120.34 | -2.6 | done | losing for real |
| coinflip | 1776 | 50.1 | 50.8 | $-942.29 | -5.3% | $57.71 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1044 | 48.8 | 51.7 | $-1043.20 | -10.0% | $-43.20 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1776 | 49.6 | 51.6 | $-1315.69 | -7.4% | $-315.69 | -3.2 | done | losing for real |
| always_up | 1776 | 45.8 | 50.5 | $-2340.71 | -13.2% | $-1340.71 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2767 | 47.6 | 49.3 | $-2171.49 |
| ETH | 3080 | 47.8 | 48.8 | $-2102.98 |
| SOL | 3186 | 47.6 | 49.3 | $-2603.53 |
| XRP | 3225 | 48.5 | 49.2 | $-1835.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
