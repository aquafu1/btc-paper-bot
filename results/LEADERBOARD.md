# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1298 windows, 34629 settled trades, 434 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 682 | 34.2 | 35.3 | $-534.70 | -7.8% | $465.30 | -1.6 | done | can't tell from luck |
| value_ev10 | 1669 | 38.8 | 39.2 | $-785.98 | -4.7% | $214.02 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3474 | 50.8 | 50.2 | $-1030.94 | -3.0% | $-30.94 | -1.7 | done | can't tell from luck |
| value_ev5 | 2517 | 40.5 | 41.1 | $-1263.67 | -5.0% | $-263.67 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2903 | 49.4 | 49.4 | $-1360.39 | -4.7% | $-360.39 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2903 | 50.6 | 51.0 | $-1599.16 | -5.5% | $-599.16 | -3.0 | done | losing for real |
| trend_filter | 2049 | 48.9 | 50.5 | $-1691.96 | -8.3% | $-691.96 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3474 | 49.2 | 50.3 | $-2190.99 | -6.3% | $-1190.99 | -3.8 | done | losing for real |
| coinflip | 4986 | 50.0 | 50.1 | $-2208.53 | -4.4% | $-1208.53 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4986 | 50.4 | 51.4 | $-2864.06 | -5.7% | $-1864.06 | -4.2 | done | losing for real |
| always_up | 4986 | 47.9 | 49.3 | $-3567.40 | -7.2% | $-2567.40 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8332 | 48.0 | 48.8 | $-4817.91 |
| ETH | 8987 | 48.3 | 48.2 | $-4695.64 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
