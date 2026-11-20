# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 904 windows, 24937 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1140 | 38.2 | 39.1 | $-611.46 | -5.4% | $388.54 | -1.5 | done | can't tell from luck |
| value_ev5 | 1726 | 39.9 | 41.0 | $-1009.22 | -5.8% | $-9.22 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2107 | 49.8 | 49.8 | $-1020.84 | -4.8% | $-20.84 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2544 | 50.5 | 50.5 | $-1034.35 | -4.1% | $-34.35 | -2.1 | done | losing for real |
| trend_filter | 1478 | 49.9 | 51.0 | $-1036.01 | -7.0% | $-36.01 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2107 | 50.2 | 50.9 | $-1295.90 | -6.2% | $-295.90 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2544 | 49.5 | 50.4 | $-1372.57 | -5.4% | $-372.57 | -2.7 | done | losing for real |
| coinflip | 3609 | 50.2 | 50.3 | $-1609.66 | -4.5% | $-609.66 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3609 | 51.2 | 51.7 | $-1679.24 | -4.7% | $-679.24 | -2.9 | done | losing for real |
| always_up | 3609 | 46.9 | 49.6 | $-3536.91 | -9.8% | $-2536.91 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5682 | 48.3 | 49.1 | $-3073.58 |
| ETH | 6198 | 48.2 | 48.5 | $-3766.41 |
| SOL | 6513 | 48.2 | 48.6 | $-3738.18 |
| XRP | 6544 | 48.3 | 48.5 | $-3729.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
