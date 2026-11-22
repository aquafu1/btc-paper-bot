# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1048 windows, 29066 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 543 | 34.4 | 35.1 | $-325.47 | -6.0% | $674.53 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2948 | 51.2 | 50.5 | $-799.21 | -2.7% | $200.79 | -1.5 | done | can't tell from luck |
| value_ev10 | 1344 | 37.4 | 39.2 | $-1046.04 | -7.8% | $-46.04 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2480 | 49.7 | 49.6 | $-1168.15 | -4.7% | $-168.15 | -2.3 | done | losing for real |
| trend_filter | 1737 | 49.3 | 50.7 | $-1358.44 | -7.8% | $-358.44 | -3.3 | done | losing for real |
| value_ev5 | 2034 | 39.3 | 41.0 | $-1481.77 | -7.3% | $-481.77 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2480 | 50.3 | 51.0 | $-1575.77 | -6.4% | $-575.77 | -3.2 | done | losing for real |
| coinflip | 4184 | 50.5 | 50.3 | $-1673.58 | -4.0% | $-673.58 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2948 | 48.8 | 50.3 | $-2056.68 | -7.0% | $-1056.68 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4184 | 50.8 | 51.5 | $-2262.63 | -5.4% | $-1262.63 | -3.6 | done | losing for real |
| always_up | 4184 | 47.3 | 49.4 | $-3645.14 | -8.7% | $-2645.14 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6626 | 48.3 | 49.0 | $-3564.26 |
| ETH | 7200 | 48.1 | 48.5 | $-4554.81 |
| SOL | 7587 | 48.1 | 48.5 | $-4517.90 |
| XRP | 7653 | 48.1 | 48.3 | $-4755.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
