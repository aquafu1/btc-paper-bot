# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 903 windows, 24924 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1139 | 38.3 | 39.1 | $-601.46 | -5.3% | $398.54 | -1.4 | done | can't tell from luck |
| value_ev5 | 1725 | 39.9 | 41.0 | $-999.22 | -5.8% | $0.78 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2543 | 50.5 | 50.5 | $-1024.35 | -4.0% | $-24.35 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2106 | 49.8 | 49.8 | $-1030.62 | -4.9% | $-30.62 | -2.3 | done | losing for real |
| trend_filter | 1477 | 49.8 | 51.0 | $-1045.79 | -7.1% | $-45.79 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2106 | 50.2 | 50.8 | $-1285.90 | -6.1% | $-285.90 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2543 | 49.5 | 50.4 | $-1382.35 | -5.4% | $-382.35 | -2.8 | done | losing for real |
| coinflip | 3607 | 50.2 | 50.3 | $-1589.66 | -4.4% | $-589.66 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3607 | 51.2 | 51.7 | $-1679.02 | -4.7% | $-679.02 | -2.9 | done | losing for real |
| always_up | 3607 | 46.9 | 49.6 | $-3516.91 | -9.8% | $-2516.91 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5677 | 48.3 | 49.1 | $-3023.58 |
| ETH | 6198 | 48.2 | 48.5 | $-3766.41 |
| SOL | 6505 | 48.2 | 48.6 | $-3737.31 |
| XRP | 6544 | 48.3 | 48.5 | $-3729.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
