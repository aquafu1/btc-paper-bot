# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 355 windows, 9564 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 7:45 PM | too few trades (186/200) |
| value_ev10 | 462 | 40.0 | 40.3 | $-203.25 | -4.4% | $796.75 | -0.8 | done | can't tell from luck |
| value_ev5 | 686 | 41.5 | 42.0 | $-343.24 | -5.0% | $656.76 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 949 | 52.1 | 52.0 | $-398.27 | -4.2% | $601.73 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 784 | 51.4 | 52.0 | $-403.05 | -5.1% | $596.95 | -1.5 | done | can't tell from luck |
| trend_filter | 528 | 47.9 | 50.4 | $-490.19 | -9.3% | $509.81 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 784 | 48.6 | 49.7 | $-521.46 | -6.7% | $478.54 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 949 | 47.9 | 49.7 | $-721.96 | -7.6% | $278.04 | -2.4 | done | losing for real |
| coinflip | 1412 | 50.1 | 50.8 | $-750.32 | -5.3% | $249.68 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1412 | 49.4 | 51.5 | $-1087.58 | -7.7% | $-87.58 | -3.0 | done | losing for real |
| always_up | 1412 | 46.5 | 50.6 | $-1670.27 | -11.8% | $-670.27 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2143 | 47.3 | 49.3 | $-1750.48 |
| ETH | 2409 | 47.6 | 48.8 | $-1732.05 |
| SOL | 2478 | 48.1 | 49.4 | $-1848.30 |
| XRP | 2534 | 48.8 | 49.1 | $-1317.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
