# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1105 windows, 30574 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 583 | 34.3 | 35.1 | $-381.49 | -6.5% | $618.51 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3083 | 51.2 | 50.4 | $-828.60 | -2.7% | $171.40 | -1.5 | done | can't tell from luck |
| value_ev10 | 1427 | 37.8 | 39.1 | $-951.09 | -6.7% | $48.91 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2598 | 49.8 | 49.4 | $-1061.73 | -4.1% | $-61.73 | -2.1 | done | losing for real |
| trend_filter | 1806 | 49.4 | 50.4 | $-1305.44 | -7.2% | $-305.44 | -3.1 | done | losing for real |
| value_ev5 | 2160 | 39.9 | 41.0 | $-1317.31 | -6.1% | $-317.31 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2598 | 50.2 | 51.1 | $-1710.29 | -6.6% | $-710.29 | -3.4 | done | losing for real |
| coinflip | 4412 | 50.4 | 50.2 | $-1717.44 | -3.9% | $-717.44 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3083 | 48.8 | 50.2 | $-2072.84 | -6.7% | $-1072.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4412 | 50.7 | 51.4 | $-2299.26 | -5.2% | $-1299.26 | -3.6 | done | losing for real |
| always_up | 4412 | 47.5 | 49.3 | $-3597.05 | -8.2% | $-2597.05 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7002 | 48.4 | 49.0 | $-3509.75 |
| ETH | 7570 | 48.2 | 48.4 | $-4529.07 |
| SOL | 7959 | 48.1 | 48.4 | $-4468.02 |
| XRP | 8043 | 48.2 | 48.2 | $-4735.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
