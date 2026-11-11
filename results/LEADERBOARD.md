# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 75 windows, 1872 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 130 | 62.3 | 52.6 | $+207.51 | +16.0% | $1207.51 | +1.9 | Wed 7:45 PM | too few trades (130/200) |
| momentum_5m_0.00pct | 293 | 56.0 | 50.9 | $+189.47 | +6.5% | $1189.47 | +1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 176 | 57.4 | 52.0 | $+142.16 | +8.1% | $1142.16 | +1.1 | Wed 12:30 PM | too few trades (176/200) |
| value_ev10 | 101 | 42.6 | 39.5 | $+9.52 | +0.9% | $1009.52 | +0.1 | Thu 4:00 AM | too few trades (101/200) |
| value_ev20 | 42 | 33.3 | 35.7 | $-43.85 | -10.4% | $956.15 | -0.5 | Sat 7:30 AM | too few trades (42/200) |
| value_ev5 | 140 | 40.7 | 41.1 | $-88.07 | -6.3% | $911.93 | -0.6 | Wed 5:45 PM | too few trades (140/200) |
| trend_filter | 98 | 43.9 | 48.6 | $-129.47 | -13.2% | $870.53 | -1.3 | Thu 5:15 AM | too few trades (98/200) |
| coinflip | 293 | 50.5 | 51.5 | $-159.98 | -5.5% | $840.02 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 176 | 42.6 | 49.3 | $-287.58 | -16.3% | $712.42 | -2.2 | Wed 12:30 PM | too few trades (176/200) |
| momentum_60m_0.30pct | 130 | 37.7 | 48.5 | $-317.99 | -24.5% | $682.01 | -2.8 | Wed 7:45 PM | too few trades (130/200) |
| always_up | 293 | 44.0 | 50.2 | $-457.24 | -15.6% | $542.76 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 394 | 47.0 | 49.7 | $-164.56 |
| ETH | 446 | 46.2 | 48.4 | $-299.18 |
| SOL | 512 | 49.2 | 48.1 | $-247.09 |
| XRP | 520 | 50.2 | 48.3 | $-224.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
