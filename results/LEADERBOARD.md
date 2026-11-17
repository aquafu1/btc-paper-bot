# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 595 windows, 16448 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1391 | 51.2 | 49.6 | $-212.68 | -1.5% | $787.32 | -0.6 | done | can't tell from luck |
| value_ev20 | 323 | 34.4 | 35.2 | $-232.82 | -7.2% | $767.18 | -1.0 | done | can't tell from luck |
| trend_filter | 954 | 50.2 | 51.0 | $-548.37 | -5.7% | $451.63 | -1.8 | done | can't tell from luck |
| value_ev10 | 773 | 38.0 | 39.4 | $-579.08 | -7.5% | $420.92 | -1.7 | done | can't tell from luck |
| value_ev5 | 1156 | 40.5 | 41.2 | $-675.39 | -5.8% | $324.61 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1672 | 50.8 | 51.0 | $-791.37 | -4.7% | $208.63 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1672 | 49.2 | 49.9 | $-949.79 | -5.7% | $50.21 | -2.3 | done | losing for real |
| coinflip | 2372 | 50.0 | 50.5 | $-1196.60 | -5.0% | $-196.60 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1391 | 48.8 | 51.3 | $-1344.80 | -9.7% | $-344.80 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2372 | 50.3 | 51.8 | $-1557.12 | -6.6% | $-557.12 | -3.3 | done | losing for real |
| always_up | 2372 | 47.2 | 49.8 | $-2219.79 | -9.4% | $-1219.79 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3735 | 48.0 | 49.2 | $-2508.95 |
| ETH | 4102 | 48.0 | 48.6 | $-2622.80 |
| SOL | 4278 | 47.9 | 48.7 | $-2920.11 |
| XRP | 4333 | 48.5 | 48.6 | $-2255.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
